from flask import Blueprint
from src.python.config.appConfig import wsApp


routes: Blueprint = Blueprint("ws", __name__)


@wsApp.on("message")
def handle_message(message: str) -> str:
    wsApp.emit("response", message)
    return message


@wsApp.on('connect')
def handle_connect() -> None:
    print('connection established with client')


@wsApp.on('disconnect')
def handle_connect() -> None:
    print('client disconnected')
