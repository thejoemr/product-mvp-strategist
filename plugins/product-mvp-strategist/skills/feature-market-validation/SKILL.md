---
name: feature-market-validation
description: Investiga online el valor comercial de cada feature de un producto para un segmento específico, triangulando competidores, precios, clientes y señales de demanda sin inventar evidencia.
---

# Feature Market Validation

## Misión

Para cada feature del inventario, contestar: **¿es necesaria o monetizable en el mercado objetivo HOY, está resuelta de forma más simple por alternativas y qué evidencia sustenta un recorte de alcance?**. Aun cuando el valor no esté confirmado, documenta su incertidumbre.

## Protocolo de búsqueda

1. Define segmento comprador, región, caso principal, categoría del producto y fecha de consulta. Nunca investigues una feature descontextualizada.
2. Agrupa features en clusters para búsquedas eficientes (por ejemplo, onboarding, captura, informes, colaboración, billing). Aun así, mapea evidencia **individualmente por ID de feature**.
3. Consulta fuentes primarias para **qué ofrece/vende el competidor y a qué precio**: web oficial, documentación, matriz de planes, demo pública, condiciones. Para **valor percibido y fricción**, busca señales independientes: reseñas detalladas, foros públicos originales, evaluaciones publicadas, problemas reportados y testimonios específicos, indicando sesgos.
4. Para decisiones de alto impacto, intenta **triangular al menos dos tipos independientes de evidencia** (oferta comercial + experiencia real/uso o compra). Si solo hay una fuente, declara nivel bajo. Lo que falta no se inventa.
5. Captura `feature_id`, segmento, competidor/alternativa, fuente/título, URL, consultado-en ISO, publicado-en si aplica, hecho puntual, tipo (`oferta`, `precio`, `dolor`, `uso`, `compra`, `regulación`), pertinencia, sesgo, conclusión y límite. Distingue hechos de inferencias.
6. Contrasta alternativas «sin feature», «feature estándar simple» y «feature avanzada». ¿Cuál es el **mínimo aceptable** para pagar/seguir usando? Considera diferencial competitivo y barreras de switching; competir por mínima superficie NO siempre vence.
7. Estima certeza `Fuerte` (evidencia directa de clientes/ventas y fuentes consistentes), `Media` (señales independientes congruentes), `Débil` (solo paridad de competidores u opiniones sueltas), `Sin evidencia` o `Sin acceso web`.
8. Conecta cada conclusión al recorte: `Mantener`, `Reducir`, `Unificar`, `Automatizar`, `Posponer`, `Retirar`, `Validar`; nunca un «lo hacen todos» como justificación suficiente.

## Integridad de investigación

- Fuente oficial que lista una feature no prueba ventas atribuibles a ella.
- Ausencia en una página de precios no prueba que una función no exista ni que nadie la pague.
- No generalices precios de región/moneda/fecha ni presentes snapshots obsoletos como actuales.
- Si se bloquea web o no hay búsqueda disponible: **«Valor online no verificado; investigación pendiente»**; no sustituyas por memoria interna ni links imaginados. Recomienda fuentes/consultas a ejecutar más adelante.
- No envíes nombres de clientes, tablas privadas, secretos, código propietario o datos sensibles como cadenas de búsqueda.

Usa [references/market-evidence-rubric.md](references/market-evidence-rubric.md). Devuelve hallazgos por ID para combinarlos con código y tesis.

## Intercambio en conversación

Trabaja en modo lectura: no crees ni edites archivos, reportes o notas persistentes, ni siquiera temporales. Devuelve el análisis como texto en el chat al agente que te invocó o al usuario si trabajas en la conversación principal.

Recibe la pregunta concreta, el contexto y los acuerdos previos. Distingue hechos, hipótesis y recomendaciones; una propuesta del especialista no es un acuerdo del usuario. Devuelve hallazgos con F-IDs, evidencia, cobertura, alternativas y la decisión pendiente que importa para continuar. Si falta información, señala la pregunta al agente principal; no bloquees un subagente esperando hablar con el usuario.

En la conversación principal, presenta primero lo que permita decidir, pregunta por la elección relevante y espera la respuesta antes de asumirla. Conserva acuerdos y pendientes en el contexto y amplía el detalle por bloques o cuando el usuario lo solicite.
