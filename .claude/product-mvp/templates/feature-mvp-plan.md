# Auditoría de producto → MVP comercializable

**Ruta elegida y motivo:** [docs/product/mvp/feature-mvp-plan.md o .agents/docs/audits/mvp/feature-mvp-plan.md; razón]  
**Proyecto:** [nombre]  
**Repositorio/commit analizado:** [URL/ruta y hash si existe]  
**Fecha y zona horaria:** [ISO]  
**Segmento comprador elegido:** [quién y dónde]  
**Cobertura del código:** [n areas examinadas / areas pendientes]  
**Cobertura del mercado:** [n features con evidencia verificada / total; fecha consulta]  
**Fuentes comerciales internas consultadas:** [contratos, telemetría, entrevistas, ninguna]  
**Limitaciones:** [restricciones del análisis]

## 1. Lista de decisiones: una fila por feature (entregable principal)

> Ordena por P0, P1, P2. **Incluye TODAS las features inventariadas**, incluso las nucleares, las que se mantienen y las no verificadas. Cada frase debe señalar un cambio concreto, no un deseo abstracto.

| ID | Feature / rol de negocio | Hoy (evidencia de código) | Cambio concreto para versión mínima | Acción | Valor de mercado (fuente / certeza) | Efecto en negocio | Prioridad |
|---|---|---|---|---|---|---|---|
| F-001 | ... | ... `[ruta:símbolo]` | Mantener X; quitar Y; fusionar Z con A | REDUCIR | [Fuente](https://...) · interpretación, grado de confianza / o SIN EVIDENCIA | ... | P0 |

**Resumen de acciones:** MANTENER [N]; REDUCIR [N]; FUSIONAR [N]; AUTOMATIZAR [N]; POSPONER [N]; RETIRAR [N]; VALIDAR [N].  
**Qué cambia conceptualmente:** [¿Qué problemas/segmentos sobregeneralizados dejan de resolverse?]  
**Qué no puede desaparecer:** [resultado nuclear / seguridad / integridad / obligaciones / ingresos].

## 2. Tesis de producto y principio de comercialización

- **Comprador:** [...]; **usuario:** [...]; **beneficiario:** [...].
- **Dolor/alternativa:** [...].
- **Promesa nuclear:** [...].
- **Job to be done:** [...].
- **Momento de primer valor:** [...].
- **Justificación para pagar:** [evidencia o HIPÓTESIS].
- **Modelo de cobro:** [implementado/hipótesis].
- **Restricciones no negociables:** [...].
- **Incertidumbres críticas:** [...].

## 3. Fichas por feature (repetir para TODAS)

### F-001 · [nombre] · [REDUCIR]

**Actor y rol de negocio:** [...].  
**Implementación comprobada:** [..., referencias `ruta:línea/símbolo`]; **cobertura:** [COMPLETA/PARCIAL/NO_VERIFICADA].  
**Objetivo que debe permanecer:** [...].

**Alcance actual:** [operaciones / estados / modos / permisos / variantes / interfaces / dependencias].

**Sobrealcance encontrado:** [premisa excesiva; por qué atiende más escenarios que el segmento MVP necesita].

**Versión mínima candidata:** [entrada indispensable → regla mínima → salida suficiente + garantías].

**Cambios concretos:**
- [ELIMINAR/FUSIONAR/DERIVAR/POSPONER ...], porque [necesidad comercial no validada] y con [riesgo/condición].
- [...].

**Evidencia online:** [fuente 1: URL, título/emisor, consultado-en, afirmación, pertinencia, limitación]; [fuente 2 si disponible]. **Fuerza:** [FUENTE_VERIFICADA/EVIDENCIA_DEBIL/SIN_EVIDENCIA/SIN_ACCESO_WEB].

**Impacto esperado:** [activación/conversión/retención/costo de IA/storage/soporte], etiquetar HIPÓTESIS si procede.

**Efectos de segundo orden:** [otras features, migración, contratos, integraciones, coherencia de recorridos].

**Lo que se conserva por seguridad/valor:** [...]. **Riesgo y reversibilidad:** [...].

**Prueba de aceptación del recorte:** Dado [...], cuando [...], entonces [resultado núcleo, con garantías].

**Experimento de negocio:** [...]; **umbral de decisión:** [...]; **confianza:** [ALTA/MEDIA/BAJA]; **prioridad:** [P0/P1/P2].

_Repetir ficha F-002, F-003..._

## 4. Cadena de valor del MVP reconstituido

`descubrimiento/adquisición → acceso → primera acción → resultado útil → decisión de pago → cobro → continuidad/soporte`

Explica cada paso, qué F-IDs lo habilitan, posibles procesos manuales legítimos y costos/riesgos. Define qué valor explícito se pierde al eliminar variantes y por qué es tolerable (o requiere validación).

### Alcance por fase

- **MVP ahora:** [F-IDs y subalcance mínimo].
- **Solo tras evidencia de demanda/pago:** [F-IDs y disparadores].
- **No justificado hoy:** [F-IDs, motivos e impacto].

## 5. Evidencia comercial y competencia

Tabla de datos DENTRO DE ESTE MISMO DOCUMENTO, con título, URL exacta, fecha de consulta, mercado, claim verificable, limitaciones y Feature IDs asociados. Diferencia `oferta visible` de `demanda probada`, `precios publicitados` de `ingresos observados`. No crear archivos separados.

## 6. Hipótesis de economía unitaria (sin inventar números)

**Datos constatados:** [datos y origen o «ninguno»].  
**Supuestos:** [segmento, precio, costos, adquisición, retención].  
**Desconocidos:** [CAC, churn, IA, storage, soporte ...].

`Margen de contribución/cliente = ingreso mensual neto - costo variable por cliente.`  
`Punto de equilibrio en clientes = costos fijos / margen de contribución por cliente` (solo margen positivo).  

Escenarios pesimista / base / optimista si hay supuestos defendibles. Explica sensibilidad y riesgo de costes invisibles.

## 7. Plan ordenado de validación y recorte

| Orden | F-IDs | Cambio/experimento | Prueba de que no rompe núcleo | Evidencia comercial pendiente | Decisión siguiente |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## 8. Validación de calidad del análisis

- [ ] Cada F-ID inventariado tiene fila, ficha y criterio de aceptación.
- [ ] Cada feature nuclear fue auditada internamente.
- [ ] Cada claim de mercado incluye URL verificable o una ausencia reconocida.
- [ ] Ninguna recomendación depende de ganancias inventadas.
- [ ] El producto mínimo todavía entrega el resultado prometido de extremo a extremo y tiene mecanismo viable de cobro.
- [ ] Se han protegido privacidad, autenticación/autorización, integridad, operabilidad y contratos aplicables.
- [ ] Referencias al código y límites de inspección visibles.
- [ ] La tabla principal y las fichas de este Markdown tienen exactamente los mismos F-IDs y decisiones; no se ha generado CSV.
