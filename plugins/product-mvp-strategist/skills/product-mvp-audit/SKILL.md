---
name: product-mvp-audit
description: Analiza código y mercado en conversación para acordar con el usuario el alcance mínimo comercial de un producto y sus próximos pasos, sin generar archivos.
argument-hint: "[segmento objetivo, país, pregunta o restricciones opcionales]"
disable-model-invocation: true
---

# Auditoría comercial de MVP en conversación

Contexto del usuario (opcional): $ARGUMENTS

Ejecuta este flujo **en la conversación principal**, conservando el historial y las respuestas del usuario. Lee ${CLAUDE_PLUGIN_ROOT}/agents/product-mvp-strategist.md y aplica su protocolo de análisis y diálogo; su lista de herramientas corresponde a ese agente y no cambia los permisos de esta sesión.

Raíz de recursos de esta instalación: ${CLAUDE_PLUGIN_ROOT}. Al leer el protocolo como archivo, interpreta sus referencias de recursos respecto a esta raíz. No busques los recursos del plugin dentro del producto que estás analizando.

Para aplicar directamente las skills, usa sus nombres completos: product-mvp-strategist:repository-feature-mapping, product-mvp-strategist:product-business-core, product-mvp-strategist:feature-market-validation, product-mvp-strategist:feature-scope-reduction y product-mvp-strategist:commercial-mvp-design. Para delegar, usa los nombres completos de especialistas que indica el protocolo.

1. Reutiliza el contexto disponible e inspecciona el repositorio en modo lectura. Presenta una primera lectura del producto, comprador y resultado pagable; distingue hechos de hipótesis.
2. Si una elección de segmento o promesa cambia el análisis, presenta alternativas con una recomendación y pregunta antes de asumirla como acordada. Continúa trabajo independiente cuando sea útil.
3. Usa las cinco skills especializadas o solicita hallazgos internos a los especialistas disponibles con Agent. Comparte las decisiones vigentes y recibe sus resultados como texto; tú mantienes el diálogo con el usuario.
4. Expón por bloques hallazgos y recortes HOY → MÍNIMO con F-IDs estables, referencias al código, fuentes de mercado fechadas, riesgos y criterios observables. Prioriza lo que afecta valor y cobro; no impongas un informe exhaustivo en cada respuesta.
5. Distingue recomendación de acuerdo: conserva en el contexto lo PROPUESTO, ACORDADO, DESCARTADO y PENDIENTE. Incorpora la respuesta del usuario y decide con él qué analizar, validar o priorizar después. No asumas aprobación por silencio.

**Salida exclusiva: respuestas en el chat.** No crees ni edites archivos, directorios, reportes ni bitácoras de auditoría, ni siquiera temporales. No ejecutes validadores de informes, no solicites rutas de salida ni implementes cambios. Si el usuario pide exportar o implementar, cierra el análisis con el alcance acordado y trata esa petición como una tarea separada fuera de esta skill.

La misión es **minimizar alcance sin perder el resultado por el que pagaría el cliente**. Una feature sin evidencia sigue sin validarse; usa SIN_EVIDENCIA o SIN_ACCESO_WEB según corresponda. No prometas ganancias sin ventas y costos comprobados.
