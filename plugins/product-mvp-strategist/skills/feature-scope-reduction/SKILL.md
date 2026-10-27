---
name: feature-scope-reduction
description: Reduce la premisa y el alcance interno de cada feature a su expresión mínima comercial, proponiendo cambios concretos sin romper el propósito nuclear, dependencias u obligaciones.
---

# Feature Scope Reduction — cirugía de producto

**Pregunta:** «Si solo sirviéramos al cliente inicial y su caso más valioso, ¿cuál sería el comportamiento mínimo de esta feature y qué complejidad dejaría de ser necesaria?»

## Evaluación obligatoria por feature

1. **Resultado y clasificación**: actor, JTBD, resultado observable, rol en la cadena de valor y evidencias de código y mercado.
2. **Exceso de premisa**: ¿el concepto presupone industrias, niveles de personalización, jerarquías, segmentos, modos o escenarios futuros no validados? Comienza aquí, antes de proponer quitar pantallas.
3. **Inventario interno**: estados, transiciones, entidades, configuraciones, validaciones, permisos, interfaces, variaciones, integraciones, notificaciones, subfeatures, controles y casos excepcionales.
4. **Contrato mínimo**: una frase de qué debe lograr la feature; entrada mínima, comportamiento mínimo, salida mínima y condición de éxito. Conservar controles legales, contractuales, de acceso, privacidad y calidad indispensables.
5. **Poda específica**: usa verbos claros `Eliminar`, `Fusionar`, `Fijar valor por defecto`, `Derivar`, `Reemplazar`, `Automatizar`, `Posponer`, `Validar antes de desarrollar`. Explica qué deja de hacer el usuario y qué se simplifica detrás. No te limites a «hacer más simple».
6. **Contrafactual**: demuestra que el recorrido punta a punta sigue generando el resultado que compra el usuario, aun sin variante avanzada. Si no se sostiene, revisa el recorte.
7. **Efectos colaterales**: API, persistencia, datos migrados, integraciones, clientes existentes, rol, dependencia de otra feature, experiencia, soporte, riesgos y reversibilidad.
8. **Decisión**: `MANTENER`, `REDUCIR`, `FUSIONAR`, `AUTOMATIZAR`, `POSPONER`, `RETIRAR` o `VALIDAR` (usa esas formas exactas en la tabla Markdown); confianza Alta/Media/Baja, prioridad y test de aceptación.
9. **Razón comercial**: vínculo con adquisición, activación, conversión, retención, costos operativos o confianza; si no hay números, usa descripción cualitativa y experimentos.

## Tests que no se pueden omitir

- Nuclear: ¿la feature mínima entrega lo esencial? ¿Funciona para buyer y usuario inicial?
- Pagable: ¿pueden recibir el beneficio y pagar por él? ¿se conserva un diferenciador por el que pagarían?
- Responsable: ¿no viola privacidad, autorización, integridad, accesibilidad aplicable, normativas y contratos?
- Operable: ¿maneja errores, reversión necesaria, soporte y casos relevantes sin agregar trabajo manual inviable?
- Rentable: ¿el recorte reduce esfuerzo o costo, sin introducir un costo oculto superior o disparar churn?
- Dependencias: ¿todas las features que quedan pueden consumir lo mínimo propuesto?

Una feature **nuclear nunca es intocable por dentro**. Si no puedes justificar un recorte por negocio, marca `VALIDAR` y diseña un test antes de borrarla.

Usa [references/feature-delta.md](references/feature-delta.md) para ficha de decisión y anti-patrones.

## Intercambio en conversación

Trabaja en modo lectura: no crees ni edites archivos, reportes o notas persistentes, ni siquiera temporales. Devuelve el análisis como texto en el chat al agente que te invocó o al usuario si trabajas en la conversación principal.

Recibe la pregunta concreta, el contexto y los acuerdos previos. Distingue hechos, hipótesis y recomendaciones; una propuesta del especialista no es un acuerdo del usuario. Devuelve hallazgos con F-IDs, evidencia, cobertura, alternativas y la decisión pendiente que importa para continuar. Si falta información, señala la pregunta al agente principal; no bloquees un subagente esperando hablar con el usuario.

En la conversación principal, presenta primero lo que permita decidir, pregunta por la elección relevante y espera la respuesta antes de asumirla. Conserva acuerdos y pendientes en el contexto y amplía el detalle por bloques o cuando el usuario lo solicite.
