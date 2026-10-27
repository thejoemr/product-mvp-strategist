# Publicar el plugin nativo

El marketplace vive en .claude-plugin/marketplace.json y lista el plugin de plugins/product-mvp-strategist/. Las definiciones se mantienen solo en ese plugin; el instalador anterior adapta la misma fuente.

## Verificar antes de subir

```bash
npm test
npm run validate
npm run validate:plugin
npm pack --dry-run
```

La validación nativa requiere Claude Code. Los comandos de análisis no ejecutan estos validadores ni crean archivos de auditoría.

Para probar sin instalar:

```bash
claude --plugin-dir ./plugins/product-mvp-strategist
```

En la sesión, ejecutar /product-mvp-strategist:product-mvp-audit. Verificar descubrimiento de las seis skills y seis agentes, carga de referencias desde el plugin, devolución interna de los especialistas y continuidad del diálogo sin reportes en disco.

## Publicar una actualización

1. Cambiar la versión en package.json, plugins/product-mvp-strategist/.claude-plugin/plugin.json y la entrada de .claude-plugin/marketplace.json.
2. Ejecutar las verificaciones y probar una instalación nativa aislada.
3. Subir una rama y abrir un Pull Request contra main. Integrar mediante el flujo de revisión del repositorio.
4. Tras integrar, usar el origen thejoemr/product-mvp-strategist sin sufijo. Durante las pruebas, especificar #nombre-de-rama en el origen del marketplace.
5. Actualizar los ejemplos de instalación cuando cambie la rama de distribución. Los usuarios actualizan marketplace y plugin desde /plugin.

No hace falta publicar en npm para distribuir el plugin. No se requiere una API key ni instalar un servidor MCP.

## Migración del instalador anterior

El instalador conserva su manifiesto de propiedad y sus controles de conflictos. Los usuarios pueden retirar la copia anterior con uninstall antes de adoptar el plugin; nunca borrar automáticamente archivos .claude/ ni configuraciones ajenas.

La compatibilidad npm se comprueba con npm pack --dry-run y una instalación en un proyecto temporal. La publicación npm, si se desea, es independiente del marketplace y requiere acceso al nombre del paquete en el registro.
