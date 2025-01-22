from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import init_db
from config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:8080", "http://localhost", "https://imageapi.spacetechnology.net", "https://imagebook.spacetechnology.net"]}})

    init_db(app)

    jwt = JWTManager(app)

    from api.user_api import user_bp
    from api.profile_api import profile_bp
    from api.login_api import login_bp
    from api.register_api import register_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)

    return app