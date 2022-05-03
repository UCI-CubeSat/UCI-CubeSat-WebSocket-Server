from src.python.route.webSocketRoute import routes
from src.python.config.appConfig import app, wsApp

[app.register_blueprint(route) for route in [routes]]


if __name__ == '__main__':
    wsApp.run(app, debug=True)
