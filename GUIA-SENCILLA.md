# Cómo poner el dashboard en internet (guía sencilla)

Solo vas a usar **Render** y tu **navegador**. No hace falta instalar nada raro ni usar la terminal.

---

## Qué vas a lograr

Al terminar tendrás un **link** (por ejemplo: `https://csat-dashboard.onrender.com`) que podés enviar a tu equipo. Cualquiera con el link puede ver el dashboard y actualizar los datos.

---

## Paso 1: Subir el proyecto a GitHub

**¿Qué es esto?** GitHub es una página donde se guarda código. Render (el paso 2) va a leer tu proyecto desde ahí. No hace falta saber programar; solo vas a subir una carpeta como si subieras fotos a la nube.

---

**1.1 – Entrar a GitHub**

- Abrí el navegador y andá a: **github.com**
- Si tenés cuenta, **iniciá sesión**. Si no, **creá una** (es gratis; te pide email y una contraseña).

---

**1.2 – Crear un “repositorio” (el lugar donde se guardará tu proyecto)**

- Arriba a la derecha vas a ver un botón **+**. Clic ahí.
- Elegí **“New repository”**.
- Donde dice **“Repository name”** escribí: **csat-dashboard** (o cualquier nombre que quieras; es solo para identificarlo).
- Todo lo demás dejalo como está. Bajá y dale al botón verde **“Create repository”**.

---

**1.3 – Subir los archivos del dashboard**

Después de crear el repo, GitHub te muestra una página casi vacía con instrucciones.

- Buscá el texto que dice **“uploading an existing file”** (o **“upload an existing file”**). Es un link; hacé **clic ahí**.  
  (Si no lo ves, buscá un botón **“Add file”** y después **“Upload files”**.)
- Se abre una zona donde podés **arrastrar archivos y carpetas**.

En tu computadora:

- Andá a **Descargas** (Downloads).
- Abrí la carpeta **csat-dashboard**.
- Seleccioná **todo** lo que hay adentro (archivos y carpetas), **excepto** la carpeta **.venv** si la ves (no hace falta subirla).  
  Archivos que sí tenés que subir: **server.py**, **index.html**, **requirements.txt**, **GUIA-SENCILLA.md**, etc.

Arrastrá todo eso a la zona de GitHub donde dice “drag files here” (o “arrastrá archivos acá”).

- Cuando termine de subir, bajá en la página y hacé clic en el botón verde **“Commit changes”** (o **“Commit new files”**).

Listo: tu proyecto ya está guardado en GitHub. En el paso 2 vas a decirle a Render que use ese proyecto.

---

## Paso 2: Crear la app en Render

1. Entrá a [render.com](https://render.com) y creá una cuenta (podés usar “Sign up with GitHub”).
2. Clic en **New +** → **Web Service**.
3. Conectá tu cuenta de GitHub si te lo pide. Elegí el repositorio **csat-dashboard** (o el nombre que hayas usado).
4. Dejá que Render rellene solo lo que pueda. Completá así:
   - **Name:** `csat-dashboard` (o el nombre que quieras para el link).
   - **Root Directory:** si todo el proyecto está en la raíz del repo, dejalo vacío. Si dentro del repo hay una carpeta `csat-dashboard`, poné: `csat-dashboard`.
   - **Build Command:**  
     `pip install -r requirements.txt`
   - **Start Command:**  
     `gunicorn -w 1 -b 0.0.0.0:$PORT server:app`
   - **Plan:** Free.

---

## Paso 3: Configurar la conexión a Redash

Render necesita dos datos para poder leer los datos del CSAT desde Redash. No se comparten con nadie; solo los usa el servidor.

1. En Redash: [redash.humand.co](https://redash.humand.co) → tu **avatar** (arriba a la derecha) → **Profile** (o **Configuración**). Ahí copiá tu **API Key**.
2. En Render, en tu Web Service, entrá a **Environment** (menú izquierdo).
3. Clic en **Add Environment Variable** y agregá estas dos:

   | Key             | Value                     |
   |-----------------|---------------------------|
   | `REDASH_URL`    | `https://redash.humand.co` |
   | `REDASH_API_KEY`| (pegá la API Key que copiaste) |

4. Guardá los cambios.

---

## Paso 4: Poner en marcha el servicio

1. En Render, dale **Create Web Service** (o **Save** si ya lo habías creado).
2. Esperá unos minutos. Render va a instalar todo y arrancar el servidor. Cuando termine, arriba te va a mostrar un link tipo:  
   `https://csat-dashboard-xxxx.onrender.com`
3. Abrí ese link en el navegador: deberías ver el dashboard. Probá el botón **Actualizar datos** para confirmar que trae datos de Redash.

---

## Después: si querés cambiar algo en el dashboard

Editás los archivos en Cursor como siempre. Para que esos cambios se vean en el link que compartiste, tenés que **subir los cambios a GitHub** (commit + push). Render toma el código de ahí y se actualiza solo. Pasos detallados en **COMO-ACTUALIZAR-CAMBIOS.md**.

---

## Compartir con tu equipo

Enviá ese link por mail, Slack o como prefieras. Cualquiera con el link puede:

- Ver el contexto del CSAT y los gráficos.
- Hacer clic en **Actualizar datos** para refrescar con la información más reciente de Redash.

No tienen que instalar nada ni tener cuenta en Render ni en Redash.

---

## Si algo no funciona

- **“Application failed to start”:** Revisá que el **Start Command** sea exactamente:  
  `gunicorn -w 1 -b 0.0.0.0:$PORT server:app`
- **“Error al cargar los datos”:** Revisá que en **Environment** estén bien puestos `REDASH_URL` y `REDASH_API_KEY` (sin espacios de más, la URL sin barra al final).
- En plan **gratis**, el servicio se “duerme” si no lo usa nadie un rato; la primera vez que alguien abra el link puede tardar 30–60 segundos en cargar. Después va normal.

Si querés, en el siguiente mensaje me contás en qué paso estás y qué ves en pantalla y te guío desde ahí.
