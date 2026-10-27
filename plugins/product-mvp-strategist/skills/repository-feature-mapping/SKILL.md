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

## Intercambio en conversación

Trabaja en modo lectura: no crees ni edites archivos, reportes o notas persistentes, ni siquiera temporales. Devuelve el análisis como texto en el chat al agente que te invocó o al usuario si trabajas en la conversación principal.

Recibe la pregunta concreta, el contexto y los acuerdos previos. Distingue hechos, hipótesis y recomendaciones; una propuesta del especialista no es un acuerdo del usuario. Devuelve hallazgos con F-IDs, evidencia, cobertura, alternativas y la decisión pendiente que importa para continuar. Si falta información, señala la pregunta al agente principal; no bloquees un subagente esperando hablar con el usuario.

En la conversación principal, presenta primero lo que permita decidir, pregunta por la elección relevante y espera la respuesta antes de asumirla. Conserva acuerdos y pendientes en el contexto y amplía el detalle por bloques o cuando el usuario lo solicite.
