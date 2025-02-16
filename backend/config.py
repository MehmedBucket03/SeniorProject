import os

# Flask settings
DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key_here")

# Database settings
#DATABASE_PATH = "database/algomatics.db"
