"""Application entrypoint used for local development.

Running this module starts a Uvicorn server that serves the
FastAPI `app` defined in `api.py`.
"""

from api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
