import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tech@786929'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///eventplanner.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'tech@786929'
