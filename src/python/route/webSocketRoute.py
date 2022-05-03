from flask import Blueprint
from datetime import datetime
from src.python.config.appConfig import wsApp


routes: Blueprint = Blueprint("ws", __name__)


@wsApp.on("message")
def handle_message(message: str) -> str:
    wsResponse = f"websocket response: {message} at {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}"
    wsApp.emit("response", wsResponse)
    return wsResponse


@wsApp.on('connect')
def handle_connect() -> None:
    print('connection established with client')


@wsApp.on('disconnect')
def handle_connect() -> None:
    print('client disconnected')
