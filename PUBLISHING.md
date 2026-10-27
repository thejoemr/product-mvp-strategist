# Publicar Product MVP Strategist

El código fuente es un proyecto listo para un repositorio GitHub **independiente y público**. Evita publicarlo como subcarpeta de un repositorio privado que contenga aplicaciones, datos o secretos: `npx` desde GitHub instala el **repositorio completo**, no una subcarpeta arbitraria.

## 1. Crear el repositorio y subirlo

Requisitos: Git, GitHub CLI (`gh`) con sesión iniciada, permisos para crear repositorios bajo la cuenta y esta carpeta descomprimida de forma independiente.

```bash
cd product-mvp-strategist
git init -b main
git add .
git commit -m "feat: initial Claude Code MVP strategist release"
gh repo create thejoemr/product-mvp-strategist --public --source=. --remote=origin --push
```

Si el repositorio ya existe vacío, utiliza en su lugar:

```bash
git remote add origin https://github.com/thejoemr/product-mvp-strategist.git
git push -u origin main
```

No incluyas credenciales en el repositorio ni en el paquete. Verifica la visibilidad **Public** y la integridad de la carpeta `.claude/` en GitHub.

## 2. Probar instalación desde GitHub

En un proyecto de prueba distinto al del harness:

```bash
npx --yes github:thejoemr/product-mvp-strategist init --dry-run
npx --yes github:thejoemr/product-mvp-strategist init
npx --yes github:thejoemr/product-mvp-strategist doctor
```

Después, abre Claude Code y ejecuta `/product-mvp-audit`.

## 3. Publicación npm (opcional)

`npx github:thejoemr/product-mvp-strategist` funciona sin publicar en npm, si el repositorio GitHub es público. Para habilitar el comando corto `npx product-mvp-strategist@latest`, primero debes tener permiso para publicar el nombre en npm. Comprueba que esté disponible:

```bash
npm view product-mvp-strategist version
npm login
npm test
npm run validate
npm publish --access public
```

**No ejecutes `npm publish` si el nombre pertenece a otra persona.** No afirmes disponibilidad npm antes de comprobar el registro.

## 4. Etiquetado y mantenimiento

Cuando el instalador, pruebas y configuración se hayan validado en Claude Code:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Para futuras versiones, actualiza `package.json`, ejecuta las pruebas, verifica comportamiento `update` sin perder personalizaciones y publica una nueva etiqueta.
