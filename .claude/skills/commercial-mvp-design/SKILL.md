---
name: commercial-mvp-design
description: Reensambla features mínimas en un MVP vendible y plantea monetización, costos unitarios, prioridades y experimentos que comprueben demanda sin prometer rentabilidad no demostrada.
---

# Commercial MVP Design

## Reensamblaje

1. A partir de cada `F-ID` y su decisión, recorre una compra plausible de principio a fin: llegada → acceso → primer valor → valor recurrente o entrega final → pago/cobro → soporte. Si falta una pieza, no es todavía un MVP vendible; anótala como feature **mínima** o proceso manual explícito con costo.
2. Conserva únicamente roles, pasos, estados, datos, límites y mecanismos necesarios para el **primer segmento**. Mantén obligaciones y diferenciadores de venta; no diseñes para segmentos no elegidos.
3. Define tres fronteras de producto: `MVP ahora`, `Posterior al primer pago` y `No justificado`; cada una debe enlazar a los IDs existentes. No inventes features nuevas como si estuvieran implementadas; etiqueta las capacidades nuevas requeridas.
4. Prioriza por importancia en la cadena de valor, sensibilidad del buyer, certeza de mercado, reducción esperada de complejidad/costo, riesgo y reversibilidad. **No inventes puntajes numéricos**; usa P0/P1/P2 y razón.

## Economía sin ficción

Distingue **valores conocidos**, **supuestos** y **desconocidos**. Cuando haya datos, presenta escenarios pesimista/base/optimista e intervalos; si no hay datos suficientes, presenta fórmulas y sensibilidad:

- `Ingresos mensuales = clientes activos pagos × ingreso medio por cliente (neto de descuentos/reembolsos)`.
- `Margen de contribución por cliente = ingreso neto por cliente − costo variable atribuible (IA, storage, envío, pagos, soporte proporcional, etc.)`.
- `Resultado operativo aproximado = clientes × margen contribución − costos fijos relevantes` (sin sustituir contabilidad formal).
- `Punto de equilibrio ≈ costos fijos / margen contribución por cliente`, **solo** si este es positivo y las unidades/periodos son consistentes.
- Si hay CAC demostrado: `CAC payback ≈ CAC / margen mensual por cliente`, si aplica y margen positivo.

No presentes ROI, LTV, TAM, churn, tasa de conversión o ingresos proyectados con precisión que los datos no permiten. Contempla costos inducidos por personalización y soporte.

## Diseño de experimentos

Para hipótesis críticas, especifica segmento, pregunta, test, umbral observable de éxito, plazo/costo aproximados **solo si respaldados o explicitados como estimación**, condición de fallo y decisión siguiente. Preferir pruebas de **compromiso real** (conversación comercial, precio aceptado, depósito/compra autorizada, uso repetido) sobre likes o clics. No hagas experimentos engañosos ni prometas funciones no disponibles.

## Salida

Redacta un único archivo Markdown basado en `.claude/product-mvp/templates/feature-mvp-plan.md`: cada F-ID debe estar en la tabla principal y en su ficha individual. Ordena por prioridad, incluye ruta de monetización y un roadmap reducido. Integra en ese archivo **fuentes de mercado, fechas y grado de certeza**; no generes un CSV ni documentos adicionales.

Lee [references/revenue-gates.md](references/revenue-gates.md).
