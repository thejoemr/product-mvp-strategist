---
name: repository-feature-mapping
description: Reconstruye desde un repositorio de software el inventario de features visibles y sus procesos reales, con evidencia de implementación y cobertura. Úsala antes de auditar alcance de producto o diseñar un MVP.
---

# Repository Feature Mapping

**Objetivo:** construir un mapa de **capacidades que el cliente reconoce**, no un catálogo de clases.

## Procedimiento

1. Revisa estructura de producto, README, especificaciones, rutas UI, API, contratos de aplicación, eventos, tareas, integraciones, modelos, tablas, tests y feature flags. Si hay documentación canónica declarada, consérvala como intención, **no** como sustituto de código.
2. Traza la ruta completa por caso: **actor → entrada (pantalla/API/proceso) → reglas/permisos → persistencia/integración → salida/resultado**. Busca flujos no accesibles por UI (batch, API, admin) y flujos ocultos por flags.
3. Agrupa operaciones técnicas en **features** por resultado de negocio. Desglosa internamente **subfeatures, modos, estados, excepciones, permisos, variables y configuraciones**. No confundas un CRUD con cuatro features cuando sirve al mismo resultado.
4. Por cada feature emite: ID estable `F-001`, nombre, actor, resultado, flujo principal, subcapacidades, evidencia (`ruta:línea` o `ruta:símbolo`), dependencias, estatus de disponibilidad (`implementada`, `expuesta`, `probada`, uso en producción desconocido) y **nivel de inspección** (`completo`, `parcial`, `no verificado`).
5. Construye un índice de cobertura: áreas exploradas, áreas excluidas, features inferidas y cantidad sin inspección profunda. Nunca digas que exploraste todo un monorepo si solo buscaste una carpeta.
6. Entrega al orquestador una tabla en lenguaje de producto y las rutas para examen posterior.

**Distinción esencial:** ausencia de llamadas locales no demuestra que nadie utilice la feature (puede tener consumidores remotos). Una implementación parcial no es una feature disponible.

**Límites:** solo lectura de código, pruebas y repositorio. No instales dependencias ni ejecutes tests que puedan escribir datos o llamar servicios. Ignora secretos. Para señales de negocio, cede a `product-business-core`.

Revisa las heurísticas de [references/coverage.md](references/coverage.md).
