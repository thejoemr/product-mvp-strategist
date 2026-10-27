#!/usr/bin/env python3
"""Valida la instalación estática del paquete de Claude Code; solo stdlib."""
import re
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
    agent_dir = root / '.claude/agents'
    skill_dir = root / '.claude/skills'
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
        if fields['_skills'] != expected_skills: problems.append(f'{path}: skills deben ser {expected_skills}; se encontró {fields["_skills"]}')
        raw_tools = fields.get('tools','')
        tools = {t.strip() for t in re.split(r',\s*(?![^()]*\))', raw_tools)}
        if name == 'product-mvp-strategist':
            if 'Write' not in tools or not any(t.startswith('Agent(') or t=='Agent' for t in tools): problems.append(f'{path}: orquestador requiere Agent + Write')
            if 'Edit' in tools: problems.append(f'{path}: no permitir Edit')
        else:
            if tools & {'Write','Edit','Agent'}: problems.append(f'{path}: especialista con privilegio de escritura/delegación')
            if name == 'market-value-researcher' and not {'WebSearch','WebFetch'}.issubset(tools):
                problems.append(f'{path}: faltan herramientas de investigación web')
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
            expected = {'context':'fork','agent':'product-mvp-strategist','background':'false','disable-model-invocation':'true'}
            for key, val in expected.items():
                if fields.get(key) != val: problems.append(f'{path}: {key} debe ser {val}')
    required=[
        'README.md', '.claude/product-mvp/templates/feature-mvp-plan.md',
        '.claude/product-mvp/examples/feature-mvp-plan.example.md',
        '.claude/product-mvp/templates/agent-handoffs.md',
        '.claude/product-mvp/scripts/validate_feature_plan.py'
    ]
    for f in required:
        if not (root/f).is_file(): problems.append(f'Falta {f}')
    return problems

if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[3]
    errs=validate(root)
    if errs:
        print('\n'.join('ERROR: '+e for e in errs)); sys.exit(1)
    print(f'OK: {len(AGENT_SKILLS)} agentes, {len(SKILLS)} skills y plantillas presentes')
