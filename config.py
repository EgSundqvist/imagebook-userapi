import os
import yaml
from dotenv import load_dotenv

# Ladda miljövariabler från .env-filen
load_dotenv()

class Config:
    def __init__(self, env):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            env_config = config.get(env, {})

            self.SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', env_config.get('SQLALCHEMY_DATABASE_URI', ''))
            self.SQLALCHEMY_TRACK_MODIFICATIONS = False
            self.JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY_FRONTEND', env_config.get('JWT_SECRET_KEY_FRONTEND', ''))
            self.JWT_SECRET_KEY_BACKEND = os.getenv('JWT_SECRET_KEY_BACKEND', env_config.get('JWT_SECRET_KEY_BACKEND', ''))
            self.IMAGEAPI_URL = os.getenv('IMAGEAPI_URL', env_config.get('IMAGEAPI_URL', ''))
            self.CLIENT_URL = os.getenv('CLIENT_URL', env_config.get('CLIENT_URL', ''))
            self.ALLOWED_EMAILS = os.getenv('ALLOWED_EMAILS', env_config.get('ALLOWED_EMAILS', '')).split(',')

            print(f"Environment: {env}")
            print(f"SQLALCHEMY_DATABASE_URI: {self.SQLALCHEMY_DATABASE_URI}")
            print(f"JWT_SECRET_KEY: {self.JWT_SECRET_KEY}")
            print(f"JWT_SECRET_KEY_BACKEND: {self.JWT_SECRET_KEY_BACKEND}")
            print(f"IMAGEAPI_URL: {self.IMAGEAPI_URL}")
            print(f"CLIENT_URL: {self.CLIENT_URL}")
            print(f"ALLOWED_EMAILS: {self.ALLOWED_EMAILS}")

env = os.getenv('FLASK_ENV', 'Development')
print(f"Starting application in {env} environment")
config = Config(env)