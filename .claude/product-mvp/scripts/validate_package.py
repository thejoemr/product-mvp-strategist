#!/usr/bin/env python3
"""Valida la instalación estática del paquete de Claude Code; solo stdlib."""
import re
import json
import sys
from pathlib import Path

AGENT_SKILLS = {
    'product-mvp-strategist': {
        'repository-feature-mapping', 'product-business-core', 'feature-market-validation',
        'feature-scope-reduction', 'commercial-mvp-design'},
    'feature-cartographer': {'repository-feature-mapping'},
    'business-core-analyst': {'product-business-core'},
    'market-value-researcher': {'feature-market-validation'},
    'feature-scope-strategist': {'feature-scope-reduction'},
    'unit-economics-reviewer': {'commercial-mvp-design'},
}
PLUGIN_REL = Path('plugins/product-mvp-strategist')
NAMESPACE = 'product-mvp-strategist:'
SKILLS = set().union(*AGENT_SKILLS.values(), {'product-mvp-audit'})


def frontmatter(path):
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError('frontmatter ausente o inválido')
    # Este paquete utiliza YAML plano + listas de skills; no requiere paquete yaml.
    block = match.group(1)
    fields = {}
    for m in re.finditer(r'^([a-zA-Z][a-zA-Z0-9-]*):\s*(.*)$', block, re.M):
        fields[m.group(1)] = m.group(2).strip().strip('"\'')
    list_match = re.search(r'^skills:\s*\n((?:\s+- [^\n]+\n?)+)', block, re.M)
    fields['_skills'] = set(re.findall(r'^\s+-\s+([^\s]+)\s*$', list_match.group(1), re.M)) if list_match else set()
    return fields, text


def validate(root):
    root = Path(root)
    problems = []
    plugin = root / PLUGIN_REL
    agent_dir = plugin / 'agents'
    skill_dir = plugin / 'skills'
    actual_agents = {p.stem for p in agent_dir.glob('*.md')}
    if actual_agents != set(AGENT_SKILLS):
        problems.append(f'Agentes: esperados {set(AGENT_SKILLS)}, encontrados {actual_agents}')
    for name, expected_skills in AGENT_SKILLS.items():
        path = agent_dir / (name + '.md')
        if not path.exists():
            continue
        try:
            fields, body = frontmatter(path)
        except ValueError as exc:
            problems.append(f'{path}: {exc}')
            continue
        for field in ('name','description','model','tools'):
            if not fields.get(field): problems.append(f'{path}: falta {field}')
        if fields.get('name') != name: problems.append(f'{path}: name ≠ archivo')
        expected_skills = {NAMESPACE + skill for skill in expected_skills}
        if fields['_skills'] != expected_skills: problems.append(f'{path}: skills deben ser {expected_skills}; se encontró {fields["_skills"]}')
        raw_tools = fields.get('tools','')
        tools = {t.strip() for t in re.split(r',\s*(?![^()]*\))', raw_tools)}
        allowed_tools = {'Read', 'Glob', 'Grep'}
        if name == 'product-mvp-strategist':
            allowed_tools.update({'WebSearch', 'WebFetch'})
            allowed_tools.add('Agent(product-mvp-strategist:feature-cartographer, product-mvp-strategist:business-core-analyst, product-mvp-strategist:market-value-researcher, product-mvp-strategist:feature-scope-strategist, product-mvp-strategist:unit-economics-reviewer)')
            if not any(t.startswith('Agent(') for t in tools):
                problems.append(f'{path}: orquestador requiere especialistas internos con Agent')
        else:
            if name == 'market-value-researcher':
                allowed_tools.update({'WebSearch', 'WebFetch'})
            if name == 'market-value-researcher' and not {'WebSearch','WebFetch'}.issubset(tools):
                problems.append(f'{path}: faltan herramientas de investigación web')
        if tools - allowed_tools:
            problems.append(f'{path}: herramientas fuera del contrato de solo lectura: {tools - allowed_tools}')
        if not {'Read', 'Glob', 'Grep'}.issubset(tools):
            problems.append(f'{path}: faltan herramientas de lectura del repositorio')
    actual_skills = {p.parent.name for p in skill_dir.glob('*/SKILL.md')}
    if actual_skills != SKILLS: problems.append(f'Skills: esperadas {SKILLS}, encontradas {actual_skills}')
    for name in SKILLS:
        path = skill_dir / name / 'SKILL.md'
        if not path.exists():
            continue
        try:
            fields, body = frontmatter(path)
        except ValueError as exc:
            problems.append(f'{path}: {exc}')
            continue
        if fields.get('name') != name or not fields.get('description'):
            problems.append(f'{path}: name/description inválidos')
        for target in re.findall(r'\]\((references/[^)]+)\)', body):
            if not (path.parent / target).is_file(): problems.append(f'{path}: referencia inexistente {target}')
        if name == 'product-mvp-audit':
            if fields.get('disable-model-invocation') != 'true':
                problems.append(f'{path}: disable-model-invocation debe ser true')
        for key in ('context', 'agent', 'background'):
            if key in fields:
                problems.append(f'{path}: {key} separa la skill de la conversación principal')
    required = [
        root / 'README.md', plugin / 'README.md', plugin / 'LICENSE',
        plugin / 'product-mvp/templates/feature-mvp-plan.md',
        plugin / 'product-mvp/examples/feature-mvp-plan.example.md',
        plugin / 'product-mvp/templates/agent-handoffs.md',
        root / '.claude/product-mvp/scripts/validate_feature_plan.py',
    ]
    for path in required:
        if not path.is_file(): problems.append(f'Falta {path}')
    try:
        manifest = json.loads((plugin / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        package = json.loads((root / 'package.json').read_text(encoding='utf-8'))
        entry = marketplace['plugins'][0]
        if manifest['name'] != 'product-mvp-strategist' or entry['name'] != manifest['name']:
            problems.append('Nombre del plugin inconsistente')
        if entry['source'] != './plugins/product-mvp-strategist':
            problems.append('Source del marketplace no apunta al plugin del paquete')
        if not (manifest['version'] == entry['version'] == package['version']):
            problems.append('Versiones de plugin, marketplace y paquete inconsistentes')
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        problems.append(f'Manifiestos del plugin incompletos: {exc}')
    for path in plugin.rglob('*.md'):
        body = path.read_text(encoding='utf-8')
        # References must resolve from the installed plugin, not the audited project.
        for relative in re.findall(r'\$\{CLAUDE_PLUGIN_ROOT\}/([a-zA-Z0-9_./-]+)', body):
            if not (plugin / relative).is_file():
                problems.append(f'{path}: recurso de plugin inexistente {relative}')
        if re.search(r'(?<![a-zA-Z0-9_/])\.claude/(?:agents|product-mvp)/', body):
            problems.append(f'{path}: referencia a recursos relativa al proyecto auditado')
    return problems

if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[3]
    errs=validate(root)
    if errs:
        print('\n'.join('ERROR: '+e for e in errs)); sys.exit(1)
    print(f'OK: {len(AGENT_SKILLS)} agentes, {len(SKILLS)} skills y plantillas presentes')
