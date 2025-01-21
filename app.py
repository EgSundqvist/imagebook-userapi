from api import create_app
from flask_migrate import Migrate, upgrade
from db import db
from logging_config import setup_logging
import os

# Konfigurera loggning
setup_logging()


# Välj miljö baserat på FLASK_ENV variabeln
env = os.getenv('FLASK_ENV', 'Development')
print(f"Starting application in {env} environment")

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=(env == 'Development'))