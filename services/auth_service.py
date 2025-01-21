from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta, datetime, timezone
from flask import current_app
import jwt

class AuthService:
    @staticmethod
    def generate_token(user_id):
        return create_access_token(identity=str(user_id), expires_delta=timedelta(hours=1))

    @staticmethod
    def decode_token(token):
        return decode_token(token)
    
    @staticmethod
    def generate_token_for_image_api(user_id):
        secret_key = current_app.config['JWT_SECRET_KEY_BACKEND']
        expiration = datetime.now(timezone.utc) + timedelta(minutes=15)
        payload = {
            'identity': str(user_id),
            'role': 'admin',  # Inkludera rollen i payloaden
            'exp': expiration
        }
        return jwt.encode(payload, secret_key, algorithm='HS256')
    
    