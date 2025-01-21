from api import create_app
from flask_migrate import Migrate, upgrade
from db import db
from logging_config import setup_logging
import os

# Konfigurera loggning
setup_logging()

app = create_app()
migrate = Migrate(app, db)



if __name__ == "__main__":
    # Sätt FLASK_ENV till 'Development' eller 'Production' baserat på miljön
    env = os.getenv('FLASK_ENV', 'Development')  # Ändra till Development med stort D
    app.run(debug=(env == 'Development'))  # Ändra till Development med stort D
