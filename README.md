# Product MVP Strategist

> Un equipo de 6 agentes y 6 skills para Claude Code que analiza código y mercado y conversa con el usuario para acordar un **MVP comercializable**, feature por feature, sin generar archivos de auditoría.

**Objetivo:** reducir alcance injustificado, *incluido el exceso dentro de las features esenciales*, preservando el problema que el cliente paga por resolver. No promete rentabilidad: propone hipótesis que deben contrastarse con compradores, precios y costos.

## Instalación con `npx`

**Desde GitHub (disponible ahora):**

```bash
npx --yes github:thejoemr/product-mvp-strategist init
```

**Desde npm, solo si el paquete `product-mvp-strategist` fue publicado en el registro:**

```bash
npx --yes product-mvp-strategist@latest init
```

El primer comando utiliza el repositorio público de GitHub y requiere **Node.js, npm y Git instalados**. No necesita una publicación en el registro npm. El segundo comando **todavía no está disponible** hasta que se publique en npm. Para instalar desde una copia local ya descargada:

```bash
node bin/cli.js init
```

Si `npx github:...` no funciona en tu entorno, utiliza la forma explícita de npm:

```bash
npm exec --yes --package=github:thejoemr/product-mvp-strategist -- product-mvp-strategist init
```

Ejecuta el instalador **desde la raíz del proyecto que quieres auditar**. Requiere Node.js 18.18 o posterior y Claude Code. El instalador no necesita dependencias de npm, no modifica `CLAUDE.md` ni `settings.json`, ni ejecuta comandos sobre el código del producto.

### Comandos del instalador

| Comando | Efecto |
|---|---|
| `init` | Copia agentes, skills y referencias en `.claude/`, sin reemplazar personalizaciones |
| `update` | Actualiza archivos del paquete si no fueron modificados por el usuario |
| `doctor` | Verifica integridad con SHA-256 |
| `uninstall` | Quita solamente archivos instalados por el paquete |

Opciones: `--target /ruta/al/proyecto`, `--global` (instala en `~/.claude/`), `--dry-run`, `--force` (respalda los archivos conflictivos antes de sobrescribirlos o retirarlos), `--help`, `--version`.

Ejemplos:

```bash
npx --yes github:thejoemr/product-mvp-strategist init --dry-run
npx --yes github:thejoemr/product-mvp-strategist init --target ./mi-producto
npx --yes github:thejoemr/product-mvp-strategist init --global
npx --yes github:thejoemr/product-mvp-strategist doctor
```

El instalador se niega a sobrescribir archivos desconocidos y aborta sin cambios si detecta colisiones. Con `--force` deja copias en `.claude/product-mvp-user-backups/`. La desinstalación preserva cualquier archivo ajeno al paquete.

## Ejecutar en Claude Code

Abre Claude Code en el proyecto y ejecuta:

```text
/product-mvp-audit Vendo a empresas medianas de México; prioriza conseguir los primeros clientes de pago
```

El comando se ejecuta en la **conversación principal**, conservando el historial para discutir los hallazgos y decidir qué sigue. No utiliza context: fork.

También puedes ejecutar `claude --agent product-mvp-strategist` para mantener una sesión conversacional con el agente, o pedir a Claude que lo invoque como subagente interno para una pregunta concreta. En ese caso devuelve sus resultados al agente principal, que los presenta y conversa contigo.

Para instalar **esta copia local modificada** en otro proyecto, desde esta carpeta:

```powershell
node .\bin\cli.js init --target "C:\ruta\a\tu-producto"
```

Si ya existe una instalación, usa update en lugar de init. El comando npx desde GitHub descarga la versión remota; los cambios de esta copia son locales hasta que se publiquen.

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
.claude/
  agents/
    product-mvp-strategist.md      # orquestador
    feature-cartographer.md       # inventario funcional desde el código
    business-core-analyst.md      # propósito de negocio
    market-value-researcher.md    # investigación online
    feature-scope-strategist.md   # reducción de alcance por feature
    unit-economics-reviewer.md   # viabilidad económica del MVP
  skills/
    product-mvp-audit/SKILL.md    # comando /product-mvp-audit
    repository-feature-mapping/
    product-business-core/
    feature-market-validation/
    feature-scope-reduction/
    commercial-mvp-design/
  product-mvp/
    templates/                    # guías de conversación e intercambio
    scripts/                      # validadores Python opcionales
    examples/
```

El orquestador coordina los cinco especialistas cuando Claude Code permite invocarlos y aportan valor. Cada especialista devuelve texto al principal y trabaja en modo lectura. Si la delegación no está disponible, se aplican las skills directamente. Los scripts Python son herramientas de mantenimiento del paquete y de su ejemplo detallado; no se ejecutan durante la conversación ni requieren crear un informe. **Python no es necesario para instalar**.

## Desarrollo y verificación

```bash
npm test
npm run validate
npm pack --dry-run
```

También puedes ejecutar el instalador sin publicarlo:

```bash
node bin/cli.js init --target ./mi-proyecto --dry-run
```

La suite verifica seguridad de instalación, actualización, conflictos, copias de seguridad, desinstalación y contratos estáticos. **No equivale a una prueba de ejecución de agentes en Claude Code ni valida la calidad de un análisis real.**

El comando permanece en la conversación principal según la [configuración oficial de skills](https://code.claude.com/docs/en/skills). La separación entre el agente principal y los resultados internos sigue el [modelo oficial de subagentes](https://code.claude.com/docs/en/sub-agents).

## Publicación

Consulta [PUBLISHING.md](PUBLISHING.md) para crear el repositorio independiente en GitHub, verificar el comando `npx` desde el repositorio y, opcionalmente, publicar en npm.

## Licencia

MIT. Claude Code es un producto de Anthropic; este paquete no está afiliado a Anthropic.
