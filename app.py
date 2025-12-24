"""Application entrypoint that starts the ASGI server.

Run this module to launch the example FastAPI application locally
using Uvicorn.
"""

from api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
