import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS


# flask config setting
app: Flask = Flask(__name__)
CORS(app)
wsApp: SocketIO = SocketIO(app)
