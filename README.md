# Dashboard CSAT – datos en vivo desde Redash

Este dashboard se alimenta de la **query 31942** de Redash (`feedback_status = NPS_SUBMITTED`). Cada vez que cargás la página o hacés clic en **Actualizar datos**, se ejecuta la query y se muestran los números actuales.

## Cómo usarlo

1. **Entorno virtual y dependencias** (una sola vez):
   ```bash
   cd ~/Downloads/csat-dashboard
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   El cliente de Redash ya está en tu skill (`~/.cursor/skills/query-redash/`); el servidor lo invoca automáticamente.

2. **Arrancar el servidor** (activar el venv si no lo tenés activo):
   ```bash
   cd ~/Downloads/csat-dashboard
   source .venv/bin/activate
   python server.py
   ```

3. **Abrir en el navegador**:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

4. **Actualizar datos**: botón **Actualizar datos** en la esquina superior derecha (o recargar la página).

## Qué hace el servidor

- **GET /** → Sirve el `index.html` del dashboard.
- **GET /api/csat** → Ejecuta la query 31942 en Redash con `feedback_status: "NPS_SUBMITTED"`, devuelve el JSON y el dashboard calcula KPIs, gráficos y conteo de comentarios.

La query de Redash:  
[https://redash.humand.co/queries/31942?p_feedback_status=NPS_SUBMITTED](https://redash.humand.co/queries/31942?p_feedback_status=NPS_SUBMITTED)

## Compartir con el equipo (poner el dashboard en internet)

**Si no sos técnico/a:** seguí la **GUIA-SENCILLA.md** paso a paso. Es una sola opción (Render) y todo se hace desde el navegador y con copiar/pegar.

Si preferís otras plataformas o más detalle técnico, está en DEPLOY.md.
