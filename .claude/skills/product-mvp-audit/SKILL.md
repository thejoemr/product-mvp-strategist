---
name: product-mvp-audit
description: Ejecuta una auditoría integral del codebase y del mercado con varios subagentes, y entrega un plan feature por feature para reducirlo a un MVP vendible.
argument-hint: "[segmento objetivo, país o restricciones opcionales]"
disable-model-invocation: true
context: fork
agent: product-mvp-strategist
background: false
---

# Ejecutar auditoría comercial de MVP

Contexto del usuario (opcional): $ARGUMENTS

Analiza el repositorio de trabajo siguiendo tu protocolo de orquestación. No implementes cambios de código. Invoca especialistas con la herramienta `Agent` cuando esté disponible, reutilizando las skills precargadas:

1. Inventario completo de features con evidencia de implementación.
2. Núcleo y motivadores de negocio, comprador y cadena de valor pagable.
3. Investigación online **fechada**, vinculada por feature al buyer y la región.
4. Recorte específico por feature y por subfeature; distingue lo nuclear de lo excesivo.
5. MVP comercialmente coherente, hipótesis económicas, riesgos y experimentos.

El **único entregable** es un Markdown con la lista priorizada de TODAS las features, fichas individuales y evidencia de mercado en el mismo archivo. Ubícalo preferentemente en `docs/product/mvp/feature-mvp-plan.md`. Si la documentación canónica reside en `.agents/docs/`, utiliza `.agents/docs/audits/mvp/feature-mvp-plan.md`. Respeta una convención explícita ya existente y nunca sobrescribas documentos canónicos. No generes CSV, archivos secundarios ni implementaciones. Una feature sin evidencia de mercado debe marcarse como tal y no tratarse como validada.

La misión es **minimizar alcance sin perder el resultado por el que pagaría el cliente**. No prometer ganancias sin ventas/costos comprobados.
