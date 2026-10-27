#!/usr/bin/env python3
"""Valida la referencia detallada del paquete; no se ejecuta durante la auditoría conversacional.

Herramienta opcional de mantenimiento para ejemplos ya guardados, no un requisito
para las respuestas del agente. No modifica archivos.
"""
import re
import sys
from pathlib import Path

ACTIONS = {'MANTENER', 'REDUCIR', 'FUSIONAR', 'AUTOMATIZAR', 'POSPONER', 'RETIRAR', 'VALIDAR'}
PRIORITIES = {'P0', 'P1', 'P2'}
REQUIRED_SECTIONS = [
    'Lista de decisiones', 'Tesis de producto', 'Fichas por feature',
    'Cadena de valor', 'Evidencia comercial', 'Hipótesis de economía',
    'Plan ordenado', 'Validación de calidad',
]


def validate(path):
    path = Path(path)
    if not path.is_file():
        return [f'No existe la referencia Markdown: {path}']
    md = path.read_text(encoding='utf-8')
    errors = []
    if not md.startswith('# '):
        errors.append('Falta un título H1')
    for section in REQUIRED_SECTIONS:
        if not re.search(r'^##\s+\d+\.\s+[^\n]*' + re.escape(section), md, flags=re.M | re.I):
            errors.append(f'Falta sección: {section}')

    table_match = re.search(r'^##\s+1\.\s+[^\n]+\n(.*?)(?=^##\s+2\.|\Z)', md, flags=re.M | re.S)
    rows = {}
    if not table_match:
        errors.append('Falta sección 1 con inventario de decisiones')
    else:
        for line in table_match.group(1).splitlines():
            if not re.match(r'^\|\s*F-\d{3,}\s*\|', line):
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) != 8:
                errors.append(f'Fila de feature debe tener 8 celdas: {line[:72]}')
                continue
            feature_id, name, current, proposed, action, market, effect, priority = cells
            if feature_id in rows:
                errors.append(f'ID duplicado en tabla: {feature_id}')
            rows[feature_id] = action
            if action not in ACTIONS:
                errors.append(f'{feature_id}: acción inválida {action!r}')
            if priority not in PRIORITIES:
                errors.append(f'{feature_id}: prioridad inválida {priority!r}')
            for key, val in [('nombre',name),('alcance actual',current),('alcance mínimo',proposed),('evidencia mercado',market),('efecto negocio',effect)]:
                if not val or val in ('...', '-', 'TBD'):
                    errors.append(f'{feature_id}: falta {key}')
            if 'FUENTE_VERIFICADA' in market and not re.search(r'https?://\S+', market):
                errors.append(f'{feature_id}: fuente verificada sin URL')
            if not (re.search(r'https?://', market) or re.search(r'SIN_EVIDENCIA|SIN_ACCESO_WEB|HIPÓTESIS', market)):
                errors.append(f'{feature_id}: mercado sin enlace ni incertidumbre explícita')
    if not rows:
        errors.append('No hay ninguna feature F-### en la tabla principal')
    detail_match = re.search(r'^##\s+3\.\s+[^\n]+\n(.*?)(?=^##\s+4\.|\Z)', md, flags=re.M | re.S)
    if not detail_match:
        errors.append('Falta sección 3 con fichas por feature')
    else:
        features = re.findall(r'^###\s+(F-\d{3,})\b([^\n]*)', detail_match.group(1), flags=re.M)
        details = {}
        for feature_id, heading in features:
            if feature_id in details:
                errors.append(f'Ficha repetida: {feature_id}')
            details[feature_id] = heading
        for absent in sorted(rows.keys() - details.keys()):
            errors.append(f'Falta ficha detallada: {absent}')
        for extra in sorted(details.keys() - rows.keys()):
            errors.append(f'Ficha sin entrada en tabla: {extra}')
        for feature_id, heading in features:
            if feature_id in rows and re.search(r'\b(?:'+'|'.join(sorted(ACTIONS))+r')\b', heading):
                action_in_heading = next(a for a in ACTIONS if re.search(r'\b'+a+r'\b', heading))
                if action_in_heading != rows[feature_id]:
                    errors.append(f'{feature_id}: acción distinta entre tabla y ficha')

    if re.search(r'\.csv\b|feature-actions\.csv', md, re.I):
        errors.append('La referencia no debe depender de un CSV')
    return errors


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: validate_feature_plan.py <ruta-al-feature-mvp-plan.md>')
        raise SystemExit(2)
    issues = validate(sys.argv[1])
    if issues:
        print('\n'.join(f'ERROR: {issue}' for issue in issues))
        raise SystemExit(1)
    print('OK: Markdown con inventario, fichas y secciones de auditoría coherentes (no sustituye revisión humana).')
