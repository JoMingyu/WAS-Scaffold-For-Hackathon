from app import create_app
from config import Config, RemoteDBConfig

application = create_app(Config, RemoteDBConfig)
