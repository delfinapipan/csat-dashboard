# Paso a paso: actualizar el dashboard con Git

Cuando editás `index.html`, `server.py` o cualquier archivo del proyecto, los cambios están solo en tu computadora. Para que el dashboard en Render (el link que compartís) se actualice, tenés que **subir los cambios a GitHub**. Render toma el código de ahí y se actualiza solo.

---

## Desde Cursor (terminal o Source Control)

### Opción 1: Usando la terminal en Cursor

1. **Abrí la terminal en Cursor**  
   Menú **Terminal** → **New Terminal** (o `` Ctrl+` `` / `` Cmd+` ``).

2. **Andá a la carpeta del proyecto** (si no estás ya ahí):
   ```bash
   cd /Users/delfinapipan/Downloads/csat-dashboard
   ```

3. **Ver qué archivos cambiaron**
   ```bash
   git status
   ```
   Ahí ves los archivos en rojo (modificados) o en verde (nuevos).

4. **Agregar los cambios**
   ```bash
   git add .
   ```
   (El punto agrega todos los archivos modificados. Si querés solo uno: `git add index.html`.)

5. **Hacer commit (guardar en tu repo local)**
   ```bash
   git commit -m "Actualicé el texto de métricas generales"
   ```
   Cambiá el mensaje entre comillas por algo que describa tu cambio.

6. **Subir a GitHub (push)**
   ```bash
   git push
   ```
   Si es la primera vez, Git puede pedirte que configures la rama: `git push -u origin main` (o `master` si tu rama se llama así).

7. **Listo**  
   En unos minutos Render va a detectar el cambio y va a reconstruir el sitio. Entrá al link del dashboard y recargá la página.

---

### Opción 2: Usando el panel Source Control (sin terminal)

1. **Abrí Source Control**  
   Clic en el ícono de ramas en la barra izquierda, o **View** → **Source Control**, o **Cmd+Shift+G** (Mac) / **Ctrl+Shift+G** (Windows).

2. **Revisá la lista de archivos** que cambiaron (aparecen bajo “Changes”).

3. **Escribí un mensaje** en la caja “Message” (ej.: “Actualicé el texto de métricas generales”).

4. **Hacé clic en ✓ Commit** para guardar los cambios en tu repo local.

5. **Subí a GitHub**  
   Clic en **Sync** o **Push** (o el ícono de nube con flecha en la barra de abajo).

6. **Listo**  
   Render se actualiza en unos minutos. Recargá el link del dashboard.

---

## Si la carpeta no está conectada a Git

Si al hacer `git status` o al abrir Source Control te dice que “no es un repositorio Git”:

1. **Inicializá el repo** (solo una vez):
   ```bash
   cd /Users/delfinapipan/Downloads/csat-dashboard
   git init
   ```

2. **Conectalo con tu repo de GitHub**  
   En GitHub, creá un repo vacío llamado `csat-dashboard`. Después en la terminal:
   ```bash
   git remote add origin https://github.com/TU-USUARIO/csat-dashboard.git
   ```
   (Reemplazá `TU-USUARIO` por tu usuario de GitHub.)

3. **Primer commit y push**
   ```bash
   git add .
   git commit -m "Primer subida del dashboard"
   git branch -M main
   git push -u origin main
   ```
   Te va a pedir usuario y contraseña (o token) de GitHub.

---

## Resumen rápido

| Paso | Comando / acción |
|------|-------------------|
| 1 | Editar y guardar archivos en Cursor |
| 2 | `git add .` (o agregar desde Source Control) |
| 3 | `git commit -m "mensaje"` (o Commit en Source Control) |
| 4 | `git push` (o Sync/Push en Source Control) |
| 5 | Esperar unos minutos y recargar el link de Render |

Más detalle (incluyendo GitHub Desktop) en **COMO-ACTUALIZAR-CAMBIOS.md**.
