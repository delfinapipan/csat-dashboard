# Cómo hacer que los cambios del dashboard se vean en el link (Render)

Cuando editás los archivos en Cursor (por ejemplo `index.html` o `server.py`), esos cambios están solo en tu computadora. Para que el dashboard que ves en el link (Render) se actualice, tenés que **subir esos cambios a GitHub**. Render toma el código desde GitHub y se actualiza solo.

Hay dos formas de subir los cambios. Elegí la que te resulte más fácil.

---

## Opción A: Desde Cursor (con Git integrado)

Si tu carpeta `csat-dashboard` ya está conectada a GitHub (porque la subiste en el Paso 1 o porque clonaste el repo), podés usar el panel de control de versiones de Cursor.

1. **Abrí la carpeta del proyecto en Cursor**  
   Archivo → Open Folder → elegí `csat-dashboard`.

2. **Hacé tus cambios**  
   Editá `index.html`, `server.py` o lo que quieras. Guardá los archivos (Cmd+S).

3. **Abrí el panel de Source Control (control de código)**  
   - Clic en el ícono de ramas en la barra izquierda, o  
   - Menú **View** → **Source Control**, o  
   - Atajo: **Ctrl+Shift+G** (Windows) / **Cmd+Shift+G** (Mac).

4. **Verás la lista de archivos que cambiaste**  
   Aparecen bajo “Changes”. Opcional: en “Message” escribí algo corto, por ejemplo: “Actualicé el texto del dashboard”.

5. **Hacé “Commit”**  
   Clic en el botón **✓ Commit** (o “Commit” arriba de la caja del mensaje). Eso guarda los cambios en tu repositorio local.

6. **Subí los cambios a GitHub (“Push”)**  
   - Si aparece un botón **Sync** o **Push**, hacé clic ahí.  
   - O en la barra azul de abajo puede decir “Publish branch” o tener un ícono de nube con flecha; clic ahí para subir.

7. **Listo**  
   Render (si tiene activado el deploy automático) en unos minutos va a reconstruir el sitio con tus cambios. Entrá de nuevo al link del dashboard y recargá la página; deberías ver la versión nueva.

**Si Cursor te pide “inicializar repositorio” o no ves Source Control:** entonces la carpeta todavía no está vinculada a Git. En ese caso usá la Opción B (GitHub Desktop) o vinculá el repo primero (ver más abajo).

---

## Opción B: Con GitHub Desktop (sin tocar la terminal)

Si preferís una app aparte que te muestre los cambios y un botón para subir:

1. **Descargá e instalá GitHub Desktop**  
   [desktop.github.com](https://desktop.github.com)

2. **Abrí GitHub Desktop y agregá el proyecto**  
   - File → Add local repository.  
   - Elegí la carpeta `csat-dashboard` (la que editás en Cursor).  
   - Si te dice que “no es un repositorio Git”, en esa misma ventana podés elegir “create a repository” para esa carpeta (así la convertís en repo y después la conectás a GitHub).

3. **Conectar con GitHub**  
   Si el repo ya existe en GitHub (el que creaste en el Paso 1): en GitHub Desktop, Repository → Repository settings → y asegurate de que esté vinculado a ese repo de GitHub (tu usuario / csat-dashboard). Si no, “Publish repository” o “Add existing repository” según lo que te ofrezca la app.

4. **Cada vez que hagas cambios en Cursor:**  
   - Abrí GitHub Desktop.  
   - Verás los archivos que cambiaste. Abajo a la izquierda escribí un mensaje corto (ej. “Actualicé el dashboard”).  
   - Clic en **“Commit to main”**.  
   - Arriba clic en **“Push origin”** (o “Push”) para subir a GitHub.

5. **Render** se actualizará solo cuando detecte el push. Esperá unos minutos y recargá el link del dashboard.

---

## Resumen

| Dónde editás          | Dónde se suben los cambios | Dónde se ve el resultado      |
|-----------------------|----------------------------|--------------------------------|
| Cursor (tu compu)     | GitHub (commit + push)     | Render (el link que compartís)|

Mientras no hagas “commit” y “push” (desde Cursor o desde GitHub Desktop), los cambios quedan solo en tu máquina y el link de Render sigue mostrando la versión anterior.

---

## Si en el Paso 1 solo arrastraste archivos (sin usar Git)

Tu carpeta en la compu no queda "conectada" al repo. Para poder actualizar después, lo más simple: instalá **GitHub Desktop**, cloná el repo (File → Clone repository → elegí csat-dashboard) en una carpeta (ej. Documentos). A partir de ahí **abrí en Cursor esa carpeta clonada** y editá ahí; cuando termines, en GitHub Desktop hacé Commit + Push. Render se actualizará con esos cambios.
