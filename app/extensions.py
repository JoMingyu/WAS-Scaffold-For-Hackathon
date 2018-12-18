from flask_jwt_extended import JWTManager
from sqlalchemy.engine.base import Engine

jwt = JWTManager()
db_master_engine: Engine = None
db_slave_engine: Engine = None
