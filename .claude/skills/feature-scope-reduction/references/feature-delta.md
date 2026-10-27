# Ficha de delta funcional (una por feature)

```markdown
### F-00X · [Nombre] · [DECISIÓN]
**Rol para negocio:** ...
**Implementado hoy:** ... (rutas y símbolos)
**Señal del mercado:** ... (URL y límite; o «Sin evidencia»)
**Premisa sobredimensionada:** ...
**Contrato mínimo:** Dado [contexto], el usuario [actor] consigue [salida] con [garantías esenciales].
**Acciones sobre subalcance:**
- ELIMINAR [opción/estado/flujo] porque [...] (condición/impacto)
- FUSIONAR [conceptos] en [...] porque [...]
- POSPONER [variante] hasta [señal de mercado/pago]
**Conservar sí o sí:** ...
**Efectos transversales:** ...
**Cambio de resultado comercial previsto:** ... (hipótesis, no dato)
**Criterio de aceptación:** ... (observable)
**Prueba de negocio:** ...
**Riesgo y reversibilidad:** ...
**Confianza:** ...
```

## Antipatrones a detectar

- **Motor universal** para un solo proceso de negocio.
- **Roles ilimitados** cuando comprador y operador necesitan dos permisos simples; respetar autorizaciones y segregación necesaria.
- **Máquinas de estados complejas** cuando la operatividad puede derivarse por fechas o evento; no borrar auditoría requerida.
- **Generador personalizado de vistas** frente a una salida estándar que ya satisface al cliente inicial.
- **Editor completo de plantillas** para una sola estructura de datos.
- **Exportación 5 formatos** sin contratos o casos de compra distintos.
- **Automatización multicanal** cuando el primer cliente acepta un canal fiable.
- **Configuración profunda** usada para cubrir casos hipotéticos en vez de construir un camino único claro.

## Ejemplo ilustrativo, NO basado en código real

«Reportes»: Actualmente plantilla, dashboards, filtros, calendario, email, formatos. Mínimo: conclusión legible + descargar formato suficiente. Posponer dashboards y distribución programada **si** evidencia de compradores del segmento confirma que es posible consumir y pagar el resultado. Riesgo: cliente empresarial podría requerir XLSX como condición contractual; validar antes de eliminar.
