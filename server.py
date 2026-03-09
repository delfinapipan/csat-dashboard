#!/usr/bin/env python3
"""
Servidor del Dashboard CSAT. Expone los datos de la query de Redash (31942)
y sirve el dashboard.

Uso local:
    python server.py
    Abrir http://127.0.0.1:5000

Hosting (Render, Railway, etc.):
    Configurar REDASH_URL y REDASH_API_KEY en el panel del servicio.
    El servidor usa PORT si está definido.
"""

import json
import os
import subprocess
import sys
import time

try:
    from flask import Flask, jsonify, send_from_directory
except ImportError:
    print("Error: instalar Flask con: pip install flask", file=sys.stderr)
    sys.exit(1)

try:
    import requests
except ImportError:
    requests = None

app = Flask(__name__, static_folder=".", static_url_path="")

REDASH_QUERY_ID = 31942
REDASH_PARAMS = {"feedback_status": "NPS_SUBMITTED"}
REDASH_CLIENT = os.path.expanduser(
    "~/.cursor/skills/query-redash/scripts/redash_client.py"
)
POLL_INTERVAL = 2
MAX_POLL_ATTEMPTS = 150


def fetch_from_redash_env():
    """Obtiene datos desde Redash usando REDASH_URL y REDASH_API_KEY (para hosting)."""
    url = (os.environ.get("REDASH_URL") or "").rstrip("/")
    api_key = os.environ.get("REDASH_API_KEY") or ""
    if not url or not api_key or not requests:
        return None, None

    headers = {"Authorization": f"Key {api_key}", "Content-Type": "application/json"}
    try:
        resp = requests.post(
            f"{url}/api/queries/{REDASH_QUERY_ID}/results",
            headers=headers,
            json={"parameters": REDASH_PARAMS},
            timeout=30,
        )
        resp.raise_for_status()
        result = resp.json()
    except requests.exceptions.RequestException as e:
        return None, str(e)

    if "job" in result:
        job_id = result["job"]["id"]
        for _ in range(MAX_POLL_ATTEMPTS):
            r = requests.get(f"{url}/api/jobs/{job_id}", headers=headers, timeout=30)
            r.raise_for_status()
            job = r.json().get("job", r.json())
            status = job.get("status")
            if status == 3:
                query_result_id = job.get("query_result_id")
                break
            if status == 4:
                return None, job.get("error", "Error en la query")
            time.sleep(POLL_INTERVAL)
        else:
            return None, "La query tardó demasiado"
    else:
        query_result_id = result.get("query_result", result).get("id")

    r = requests.get(
        f"{url}/api/query_results/{query_result_id}",
        headers=headers,
        timeout=30,
    )
    r.raise_for_status()
    data = r.json().get("query_result", r.json())
    columns = data.get("data", {}).get("columns", [])
    rows = data.get("data", {}).get("rows", [])
    col_names = [c.get("name", c.get("friendly_name", "")) for c in columns]
    out = {"columns": col_names, "rows": rows, "row_count": len(rows)}
    return out, None


def fetch_from_redash_local():
    """Usa el script local del skill (para desarrollo)."""
    if not os.path.exists(REDASH_CLIENT):
        return None, "Cliente de Redash no encontrado"
    cmd = [
        sys.executable,
        REDASH_CLIENT,
        "run-saved",
        str(REDASH_QUERY_ID),
        "--format", "json",
        "--params", json.dumps(REDASH_PARAMS),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            return None, result.stderr or "Error al ejecutar la query"
        return json.loads(result.stdout), None
    except subprocess.TimeoutExpired:
        return None, "La query tardó demasiado"
    except json.JSONDecodeError as e:
        return None, f"Respuesta inválida: {e}"
    except Exception as e:
        return None, str(e)


def fetch_from_redash():
    """Obtiene los datos del CSAT: primero por env (hosting), sino por script local."""
    if os.environ.get("REDASH_URL") and os.environ.get("REDASH_API_KEY"):
        return fetch_from_redash_env()
    return fetch_from_redash_local()


@app.route("/api/csat")
def api_csat():
    """Devuelve los datos del CSAT desde Redash."""
    data, err = fetch_from_redash()
    if err:
        return jsonify({"error": err}), 502
    return jsonify(data)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0" if os.environ.get("PORT") else "127.0.0.1"
    print("Dashboard CSAT – datos desde Redash (query 31942)")
    print(f"Abrir: http://127.0.0.1:{port}" if host == "127.0.0.1" else f"Escuchando en puerto {port}")
    print("Ctrl+C para detener\n")
    app.run(host=host, port=port, debug=False)
