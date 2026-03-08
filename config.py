import os
from dotenv import load_dotenv

# Load environment variables from a .env file (development convenience)
load_dotenv()

class Config:
    # SECRET_KEY should be set in the environment for production.
    # A default is provided only for local development; change it before deploying.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
