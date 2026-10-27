# Auditoría de producto → MVP comercializable

**Ruta elegida y motivo:** `docs/product/mvp/feature-mvp-plan.md` — documentación de producto; ejemplo no derivado de un producto real.
**Proyecto:** Ejemplo ilustrativo sin cliente real
**Repositorio/commit analizado:** No aplicable, muestra ficticia
**Fecha y zona horaria:** 2026-10-26, America/Mexico_City
**Segmento comprador elegido:** Pequeñas empresas, HIPÓTESIS
**Cobertura del código:** No aplica a ejemplo
**Cobertura del mercado:** 0/1; SIN_EVIDENCIA
**Fuentes comerciales internas consultadas:** ninguna
**Limitaciones:** Ejemplo para probar formato; nunca usar como evidencia de mercado

## 1. Lista de decisiones: una fila por feature (entregable principal)

| ID | Feature / rol de negocio | Hoy (evidencia de código) | Cambio concreto para versión mínima | Acción | Valor de mercado (fuente / certeza) | Efecto en negocio | Prioridad |
|---|---|---|---|---|---|---|---|
| F-001 | Generación de reportes | Reportes con plantillas, filtros, envíos `[ejemplo/no verificable]` | Mantener reporte básico y posponer plantillas | REDUCIR | SIN_EVIDENCIA: validar con compradores | Menor complejidad operativa, HIPÓTESIS | P0 |

**Resumen de acciones:** REDUCIR 1, restantes 0.
**Qué cambia conceptualmente:** se acota personalización.
**Qué no puede desaparecer:** resultado consultable y protección de datos.

## 2. Tesis de producto y principio de comercialización

HIPÓTESIS: comprador busca resultados simples y comprensibles. Precio y voluntad de pago no comprobados.

## 3. Fichas por feature (repetir para TODAS)

### F-001 · Reportes · REDUCIR

**Actor y rol de negocio:** quien consulta resultados.
**Implementación comprobada:** no hay; ejemplo ficticio. **Cobertura:** NO_VERIFICADA.
**Objetivo que debe permanecer:** recibir resultado legible.
**Alcance actual:** variantes y plantillas hipotéticas.
**Sobrealcance encontrado:** personalización aún no validada.
**Versión mínima candidata:** consultar un reporte estándar.
**Cambios concretos:** POSPONER plantillas adicionales.
**Evidencia online:** SIN_EVIDENCIA; comprobar demanda antes de aplicar.
**Impacto esperado:** HIPÓTESIS de ahorro.
**Efectos de segundo orden:** revisar exportaciones.
**Lo que se conserva por seguridad/valor:** autorización y privacidad.
**Prueba de aceptación del recorte:** se genera un resultado autorizado.
**Experimento de negocio:** entrevistas pagadas; **confianza:** BAJA; **prioridad:** P0.

## 4. Cadena de valor del MVP reconstituido

Acceso → reporte básico → resultado útil → cobro hipotético.

## 5. Evidencia comercial y competencia

SIN_EVIDENCIA. No se consultaron fuentes para este ejemplo ficticio.

## 6. Hipótesis de economía unitaria (sin inventar números)

Sin precios ni costos reales, no hay evaluación cuantitativa.

## 7. Plan ordenado de validación y recorte

| Orden | F-IDs | Cambio/experimento | Prueba de que no rompe núcleo | Evidencia comercial pendiente | Decisión siguiente |
|---|---|---|---|---|---|
| 1 | F-001 | Probar reporte simple | Usuario recibe resultado | Entrevista con comprador | VALIDAR |

## 8. Validación de calidad del análisis

- [x] IDs coinciden en tabla y fichas.
- [ ] Mercado debe investigarse en un caso real.
