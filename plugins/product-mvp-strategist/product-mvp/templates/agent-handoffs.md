# Contratos de intercambio entre especialistas

Los especialistas no inventan decisiones de otros dominios. El orquestador recibe artefactos conceptuales (tablas en sus respuestas, nunca archivos) con estas estructuras mínimas:

## A. feature_cartographer → business_core_analyst y feature_scope_strategist

`feature_id | nombre funcional | actor | resultado observable | entrypoint | flujo vertical | subalcances/estados/opciones | dependencias | evidencia_codigo | cobertura`.

El cartógrafo **no** evalúa demanda ni decide eliminar.

## B. business_core_analyst → market_value_researcher y feature_scope_strategist

`segmento | comprador | JTBD | promesa_nuclear | caso_principal | camino_de_primer_valor | camino_de_cobro | límites | invariantes | hipótesis_confiabilidad`.

El analista separa evidencia documental de hipótesis, y vincula los IDs a roles `nuclear/habilitadora/comercial/retención/obligatoria/complementaria/especulativa`.

## C. market_value_researcher → feature_scope_strategist

`feature_id | mercado | señal/valor | alternativa/competidor | URL | tipo_fuente | fecha_consulta | conclusión_que_fuente_SÍ_sostiene | lo_que_NO_sostiene | certeza | hipótesis_de_recorte`.

Fuente comercial oficial para presencia/precio no equivale a resultado de ventas. Registra explícitamente `SIN_EVIDENCIA` o `SIN_ACCESO_WEB` cuando corresponda.

## D. feature_scope_strategist → orquestador

`feature_id | clasificación negocio | premisa excesiva | alcance actual | comportamiento_mínimo | recortes individuales | dependencia/impacto | prueba_nuclear | riesgo | acción | prioridad candidata | criterio_aceptacion | confianza`.

Si una poda rompe invariantes, la estrategia se vuelve `VALIDAR` o `MANTENER`, con explicación, no una eliminación agresiva.

## E. unit_economics_reviewer → orquestador

`trayecto MVP | capacidad de cobrar | modelo de ingresos observado/hipotético | fijos/variables conocidos | supuestos | sensibilidad de margen | riesgos de CAC/retención | experimentos | secuencia P0/P1/P2`.

## Reglas de reconciliación

1. El orquestador consolida una recomendación por `feature_id` y expone desacuerdos relevantes en el chat. Solo el usuario convierte una propuesta en acuerdo.
2. Prioridad del conflicto: garantías y obligaciones comprobadas → valor nuclear → compromisos comerciales verificados → demanda de mercado transferible → hipótesis reversibles.
3. Si mercado no confirma y el retiro sería irreversible, marca `VALIDAR` o propone reducir tras un piloto.
4. No hagas depender un recorte de una feature de una variante eliminada en otra: verifica caminos punta a punta con grafo de dependencias.
5. Auditoría completa: cada ID inventariado tiene una recomendación trazable en el contexto. Presentar por bloques no autoriza omitir features ni afirmar cobertura completa si quedan pendientes.

## Contexto común de cada solicitud

Comparte pregunta y alcance de la etapa, segmento/región, tesis elegida o hipótesis, acuerdos y pendientes del usuario, F-IDs aplicables y evidencia ya obtenida. El especialista devuelve texto, no rutas de entregables.

El agente principal presenta al usuario las conclusiones que requieren elección y espera su respuesta. Un subagente devuelve las preguntas al principal sin intentar abrir un diálogo propio. Conserva por F-ID el estado PROPUESTO, ACORDADO, DESCARTADO o PENDIENTE dentro de la conversación. Ningún intercambio requiere archivos, carpetas ni validadores de informes.
