# Cómo hostear el Dashboard CSAT para compartirlo con el equipo

El dashboard puede desplegarse en **Render** o **Railway**. En ambos casos el servidor necesita conectarse a Redash; para eso configurás dos variables de entorno con tu API key de Redash (no se suben al código).

---

## 1. Obtener la API key de Redash

1. Entrá a [Redash Humand](https://redash.humand.co).
2. Clic en tu avatar (arriba a la derecha) → **Profile** (o **Configuración**).
3. Copiá tu **API Key** (si no tenés, generá una).

La URL de Redash es: `https://redash.humand.co`

---

## 2. Opción A: Render (recomendado, gratis)

1. Creá una cuenta en [render.com](https://render.com) (con GitHub si tenés el repo).
2. **New** → **Web Service**.
3. Conectá el repo donde esté el `csat-dashboard` (o subí el proyecto a un repo nuevo y conectalo).
4. Configurá:
   - **Root Directory:** `csat-dashboard` (si el repo es la carpeta padre) o dejá vacío si el repo es directamente el dashboard.
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -w 1 -b 0.0.0.0:$PORT server:app`
   - **Runtime:** Python 3
5. En **Environment** agregá:
   - `REDASH_URL` = `https://redash.humand.co`
   - `REDASH_API_KEY` = (tu API key)
6. **Create Web Service**. En unos minutos te da una URL tipo `https://csat-dashboard-xxx.onrender.com`.
7. Compartí esa URL con tu equipo. Cada vez que abran o hagan “Actualizar datos”, se consulta Redash en vivo.

**Nota:** En el plan gratis, el servicio se “duerme” después de inactividad; la primera carga puede tardar unos segundos.

---

## 3. Opción B: Railway

1. Creá una cuenta en [railway.app](https://railway.app).
2. **New Project** → **Deploy from GitHub repo** (o subí el código).
3. Si hace falta, indicá que el directorio del proyecto es `csat-dashboard`.
4. En **Variables** del servicio agregá:
   - `REDASH_URL` = `https://redash.humand.co`
   - `REDASH_API_KEY` = (tu API key)
5. Railway detecta Python y usa `requirements.txt`. Si no arranca solo, configurá el comando de start: `gunicorn -w 1 -b 0.0.0.0:$PORT server:app`
6. En **Settings** → **Networking** generá un dominio público y usá esa URL para compartir.

---

## 4. Repo en GitHub (si aún no tenés)

Si el dashboard está solo en tu compu:

```bash
cd ~/Downloads/csat-dashboard
git init
git add .
git commit -m "Dashboard CSAT con datos desde Redash"
# Crear repo en github.com y luego:
git remote add origin https://github.com/TU_USUARIO/csat-dashboard.git
git branch -M main
git push -u origin main
```

Luego conectá ese repo a Render o Railway como en los pasos anteriores.

---

## Seguridad

- **No subas** la API key al repo. Usá solo variables de entorno en Render/Railway.
- La API key de Redash da acceso a las queries a las que tenga permiso tu usuario; compartir el link del dashboard es compartir *vista* de esos datos, no la key.
- Si querés restringir quién ve el dashboard, tendrías que sumar autenticación (por ejemplo con un proxy o un login básico); eso sería un paso siguiente.

---

## Resumen

| Dónde   | URL después del deploy      | Qué hace |
|--------|-----------------------------|----------|
| Render | `https://tu-app.onrender.com` | Servidor + Redash por env |
| Railway| `https://tu-app.railway.app`  | Igual |

En ambos, el equipo solo abre el link, ve el contexto del CSAT, los KPIs, gráficos e insights, y puede usar **Actualizar datos** para refrescar desde Redash.
