---
name: product-business-core
description: Infiere la razón comercial de un producto desde código y documentación, identifica comprador, trabajo a resolver, promesa nuclear, controles no negociables y ruta de monetización antes de reducir features.
---

# Product Business Core

## Contrato

El MVP no es lo que tiene menos pantallas. Es la **cadena mínima completa que entrega un resultado con valor pagable a un cliente definido**.

## Método

1. Clasifica fuentes: `D` decisión/documentación del dueño, `I` implementación, `U` uso/telemetría, `C` contratación/ventas/entrevista, `H` hipótesis. Si `product.md` es fuente canónica declarada, respeta sus intenciones pero **detecta** diferencias con la implementación y con demanda externa.
2. Deduce, por segmento, `comprador ≠ usuario ≠ beneficiario ≠ administrador` si aplica; dolor, alternativa, costo de seguir sin producto y *job to be done*.
3. Formula la promesa: **«[Segmento] paga/pagaría para lograr [resultado observable] sin [fricción/problema], mediante [mecanismo mínimo]»**. Etiqueta lo inferido como hipótesis.
4. Selecciona el **caso inicial de uso**, no un mercado universal. Si hay más de una tesis defendible, explica dos alternativas y cuál probar primero por evidencia y factibilidad; no elijas arbitrariamente una sola.
5. Construye cadena de valor: `descubrimiento → acceso → configuración imprescindible → primer valor → resultado completo → conversión/cobro → uso repetido/retención → soporte` (adapta a B2B o transacción puntual).
6. Define **invariantes**: condiciones imprescindibles del resultado, seguridad, permisos, privacidad, consistencia, normatividad, continuidad/soporte y compromisos de clientes existentes.
7. Etiqueta cada feature del inventario `nuclear`, `habilitadora`, `comercial`, `retención`, `obligación`, `complementaria` o `especulativa`. No una etiqueta por clase de software.
8. Entrega un **test de invariantes**: ante cualquier recorte, ¿puede el comprador todavía obtener y pagar por el beneficio comprometido sin romper garantías esenciales?

Nunca deduzcas intención de pago solo de una pantalla de precios ni confundas funcionalidades llamativas con valor central. Lee [references/business-thesis.md](references/business-thesis.md) para casos y distinciones.
