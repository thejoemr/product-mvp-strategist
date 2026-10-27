# Product MVP Strategist

> Un equipo de 6 agentes y 6 skills para Claude Code que analiza código y mercado y conversa con el usuario para acordar un **MVP comercializable**, feature por feature, sin generar archivos de auditoría.

**Objetivo:** reducir alcance injustificado, *incluido el exceso dentro de las features esenciales*, preservando el problema que el cliente paga por resolver. No promete rentabilidad: propone hipótesis que deben contrastarse con compradores, precios y costos.

## Instalar como plugin nativo (recomendado)

En el chat de Claude Code, ejecuta:

```text
/plugin install product-mvp-strategist --marketplace thejoemr/product-mvp-strategist#codex/conversational-mvp-workflow
```

Esta versión está disponible en la rama indicada. Cuando se integre en main, podrá omitirse el sufijo #codex/conversational-mvp-workflow.

El comando agrega el marketplace y abre la instalación del plugin. Requiere Claude Code 2.1.275 o posterior. Elige si lo quieres para tu usuario o para el proyecto y acepta la instalación. No requiere Node.js, npm ni Python.

También puedes usar la instalación en dos pasos:

```text
/plugin marketplace add thejoemr/product-mvp-strategist#codex/conversational-mvp-workflow
/plugin install product-mvp-strategist@product-mvp-tools
```

Recarga los plugins con /reload-plugins o inicia una nueva sesión de Claude Code. Después ejecuta:

```text
/product-mvp-strategist:product-mvp-audit Vendo a empresas medianas de México; prioriza los primeros clientes de pago
```

El comando conserva la conversación principal. Los especialistas devuelven sus resultados internos y el agente conversa contigo para acordar decisiones y próximos pasos.

El plugin también permite iniciar una sesión con el agente:

```bash
claude --agent product-mvp-strategist:product-mvp-strategist
```

### Actualizar o desinstalar

Usa /plugin para administrar el plugin desde las pestañas Installed y Marketplaces. Actualiza primero el marketplace y después el plugin. Si fijaste la instalación a una rama, las actualizaciones siguen esa rama.

En terminal:

```bash
claude plugin marketplace update product-mvp-tools
claude plugin update product-mvp-strategist@product-mvp-tools
claude plugin uninstall product-mvp-strategist@product-mvp-tools
```

### Si ya lo instalaste mediante npx

El plugin usa comandos con prefijo, como /product-mvp-strategist:product-mvp-audit. La instalación anterior usa /product-mvp-audit y no se elimina automáticamente. Para evitar que Claude descubra ambas copias, desinstala la anterior desde la carpeta de esta copia local del repositorio:

```powershell
node .\bin\cli.js uninstall --target "C:\ruta\a\tu-producto"
```

Si la instalación anterior fue global, usa --global en lugar de --target "C:\ruta\a\tu-producto". El desinstalador conserva archivos ajenos y se detiene ante personalizaciones; no uses --force salvo que quieras respaldarlas y retirarlas.

### Instalador anterior (opcional)

Se conserva para instalaciones sin plugins y actualizaciones de copias anteriores. Requiere Node.js 18.18+ y no modifica CLAUDE.md ni settings.json.

Desde la carpeta de este repositorio:

```powershell
node .\bin\cli.js init --target "C:\ruta\a\tu-producto"
```

Acepta init, update, doctor, uninstall, --global, --dry-run y --force (respalda personalizaciones). En esta modalidad el comando sigue siendo /product-mvp-audit. La definición del plugin es la única fuente; el instalador adapta rutas y nombres al copiarla a .claude/.

### Qué hace

1. **Reconstruye cada feature**, no solo pantallas: actores, reglas, datos, flujos, dependencias, casos especiales y pruebas que demuestren lo que realmente existe.
2. **Deduce el trabajo pagable** y las restricciones no negociables: beneficios del usuario, comprador, seguridad, confianza, compromisos, capacidad de entregar el servicio y cobro.
3. **Investiga el mercado**: alternativas, ofertas, planes, reseñas, testimonios y señales de dolor real. Diferencia «lo ofrece un competidor» de «alguien pagó por ello».
4. **Cuestiona el alcance de cada feature**, incluso si es indispensable: roles, estados, flujos, modos, configurabilidad y excepciones potencialmente excesivos.
5. **Reconstruye un MVP integrado** conservando el recorrido completo desde primer valor hasta servicio/cobro y costos sostenibles.
6. **Presenta recomendaciones por bloques en el chat** con hechos, hipótesis, acciones, riesgos y fuentes. El usuario y el agente acuerdan las decisiones y los siguientes pasos.

### Flujo de entrada y salida

La entrada es tu pregunta, el repositorio y el contexto ya acordado. La salida es texto en la conversación:

1. Una primera lectura del producto, comprador, resultado pagable y límites de inspección.
2. Hallazgos con evidencia de código y mercado, alternativas y recomendaciones HOY → MÍNIMO.
3. Una pregunta concreta para acordar la siguiente decisión: qué validar, conservar, simplificar o investigar.
4. Una síntesis de acuerdos y pendientes que se actualiza con tus respuestas.

El agente distingue PROPUESTO, ACORDADO, DESCARTADO y PENDIENTE por feature. Una recomendación no se considera aprobada por silencio y ningún recorte se implementa durante la auditoría. Si pides un análisis completo, puede cubrir todas las features por bloques dentro del chat.

**No crea archivos, reportes, CSV, bitácoras ni carpetas de auditoría, tampoco temporales.** Agente y especialistas operan en modo lectura y devuelven sus resultados en sus respuestas. Exportar o implementar corresponde a una tarea separada fuera del modo de análisis. El instalador sí copia las definiciones del paquete a .claude/; eso no es una salida de auditoría.

Si no puede investigar online, declara SIN_ACCESO_WEB y no inventa fuentes. No envía contenido privado del código a buscadores públicos. Los hallazgos comerciales son hipótesis hasta contar con compradores y mediciones reales.

## Componentes

```text
.claude-plugin/
  marketplace.json
plugins/product-mvp-strategist/
  .claude-plugin/plugin.json
  agents/                         # coordinador y cinco especialistas
  skills/                         # seis skills, incluido product-mvp-audit
  product-mvp/templates/          # guías de conversación e intercambio
  product-mvp/examples/
.claude/product-mvp/scripts/      # verificaciones de mantenimiento
bin/                             # instalador anterior, fuera del plugin
```

El plugin contiene únicamente definiciones, referencias y ejemplos. No incluye hooks, servidores MCP ni ejecutables. Los agentes operan en modo lectura. Si la delegación no está disponible, el principal aplica las skills directamente. Python solo es necesario para ejecutar las verificaciones de mantenimiento.

## Desarrollo y verificación

```bash
npm test
npm run validate
npm run validate:plugin
npm pack --dry-run
```

También puedes ejecutar el instalador sin publicarlo:

```bash
node bin/cli.js init --target ./mi-proyecto --dry-run
```

La suite verifica seguridad de instalación, actualización, conflictos, copias de seguridad, desinstalación y contratos estáticos. **No equivale a una prueba de ejecución de agentes en Claude Code ni valida la calidad de un análisis real.**

El comando permanece en la conversación principal según la [configuración oficial de skills](https://code.claude.com/docs/en/skills). La separación entre el agente principal y los resultados internos sigue el [modelo oficial de subagentes](https://code.claude.com/docs/en/sub-agents).

## Publicación

Consulta [PUBLISHING.md](PUBLISHING.md) para mantener el marketplace, publicar actualizaciones y comprobar la instalación nativa.

## Licencia

MIT. Claude Code es un producto de Anthropic; este paquete no está afiliado a Anthropic.
