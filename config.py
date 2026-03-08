import os
from dotenv import load_dotenv

# Load .env in development so I can keep secrets out of source control
load_dotenv()


class Config:
    # Put a real secret into the environment before deploying
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
