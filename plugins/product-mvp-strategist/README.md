# Product MVP Strategist

Plugin de Claude Code con seis agentes y seis skills para analizar código y mercado y acordar un MVP comercializable en la conversación.

## Instalación

En el chat de Claude Code 2.1.275 o posterior:

```text
/plugin install product-mvp-strategist --marketplace thejoemr/product-mvp-strategist#codex/conversational-mvp-workflow
```

Recarga los plugins con /reload-plugins o inicia una nueva sesión. Administra las actualizaciones y la desinstalación desde /plugin.

## Uso

Con el plugin instalado, ejecuta en el chat:

```text
/product-mvp-strategist:product-mvp-audit
```

Puedes añadir segmento, región y restricciones. El análisis presenta hallazgos, evidencia, alternativas y una pregunta concreta para decidir el siguiente paso contigo.

La auditoría trabaja en modo lectura. No genera archivos, reportes ni implementaciones. Los especialistas devuelven sus hallazgos al agente principal y este mantiene el diálogo con el usuario. Las recomendaciones no se consideran acordadas por silencio.

## Componentes

- Seis agentes en agents/, incluido el coordinador product-mvp-strategist.
- Seis skills en skills/, incluida product-mvp-audit.
- Guías de intercambio y ejemplos en product-mvp/.

No requiere Node.js, npm ni Python para usar el plugin. No contiene hooks, servidores MCP ni comandos de instalación. Usa las herramientas disponibles en Claude Code; si la investigación web no está disponible, declara esa limitación.

Consulta el README del repositorio para instalación, actualización y migración desde la versión npx.
