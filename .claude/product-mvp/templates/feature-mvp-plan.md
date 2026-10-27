# Guía de conversación sobre el alcance del MVP

Referencia interna para ordenar respuestas en el chat. No copiarla a un informe ni crear archivos a partir de ella. Adaptar el nivel de detalle a la pregunta actual.

## Primera devolución

Presenta qué producto observas, para quién parece ser y qué resultado pagable ofrece. Separa hechos de hipótesis y señala qué áreas inspeccionaste. Si hay una elección de segmento pendiente, expón alternativas, recomienda una por evidencia y pregunta antes de fijarla.

## Discusión por feature

Usa una tabla breve si ayuda a comparar el bloque actual:

| ID | Hoy y evidencia | Mínimo propuesto | Acción recomendada | Riesgo / certeza | Estado en la conversación |
|---|---|---|---|---|---|
| F-001 | [capacidad y ruta:símbolo] | [entrada → comportamiento → resultado] | [MANTENER/REDUCIR/FUSIONAR/AUTOMATIZAR/POSPONER/RETIRAR/VALIDAR] | [dependencia, fuente o SIN_EVIDENCIA] | PROPUESTO |

Conserva F-IDs estables entre turnos. El estado es PROPUESTO, ACORDADO, DESCARTADO o PENDIENTE; solo una respuesta explícita del usuario autoriza marcar ACORDADO. Acción recomendada y estado del acuerdo son campos distintos.

Para una recomendación de impacto, explica:

- Resultado que se conserva y exceso concreto que se propone recortar.
- Evidencia de código y mercado: URL, fuente, fecha, pertinencia y límites; o SIN_EVIDENCIA / SIN_ACCESO_WEB.
- Efectos en dependencias, cobro, entrega, soporte, seguridad y compromisos.
- Criterio observable de aceptación, reversibilidad y validación pendiente.
- Alternativas, recomendación razonada y pregunta que desbloquea el próximo paso.

No exijas una ficha exhaustiva por feature en cada respuesta. Si el usuario pide el detalle completo, puedes usar las categorías del ejemplo detallado en .claude/product-mvp/examples/feature-mvp-plan.example.md, siempre dentro del chat.

## Cierre de etapa

Resume acuerdos y pendientes, qué puede hacer el cliente con el MVP candidato, qué falta comprobar y qué experimento conviene realizar después. Distingue costos constatados, supuestos y desconocidos. Ninguna recomendación se considera implementada.

Termina con la decisión concreta que el usuario debe tomar, o con el siguiente paso que ya acordó. Cuando actúes como subagente, devuelve esa pregunta al principal para que la plantee al usuario.
