from src.python.route.webSocketRoute import routes
from src.python.config.appConfig import app, wsApp

_ = [app.register_blueprint(route) for route in [routes]]


if __name__ == '__main__':
    wsApp.run(app, debug=True, port="5001")
