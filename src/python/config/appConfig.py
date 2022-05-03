import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

# flask config setting
flaskHost: str | None = os.getenv("FLASK_HOST") if os.getenv("FLASK_HOST") else None
flaskPort: str | None = os.getenv("FLASK_PORT") if os.getenv("FLASK_PORT") else None
flaskEnv: str | None = os.getenv("FLASK_ENV") if os.getenv("FLASK_ENV") else "development"
flaskDebug: bool = True if flaskEnv == "development" else False

app: Flask = Flask(__name__)
CORS(app)
wsApp: SocketIO = SocketIO(app)
