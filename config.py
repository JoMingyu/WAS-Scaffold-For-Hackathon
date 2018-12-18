import os
from datetime import timedelta

_DB_HOST_FORMAT = 'mysql_pymysql://{username}:{password}@{host}/{dbname}?charset=utf8mb4'


def _build_db_host(username, password, host, dbname):
    return _DB_HOST_FORMAT.format(username, password, host, dbname)


class Config:
    RUN_SETTING = {
        'host': 'localhost',
        'port': 5000,
        'debug': True,
        'threaded': True
    }
    # uWSGI를 통해 배포되어야 하므로, production level에선 run setting을 건드리지 않음

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    JWT_HEADER_TYPE = ''


class LocalDBConfig:
    DB_HOSTS = {
        'master': _build_db_host('', '', '', '')
    }


class RemoteDBConfig:
    DB_HOSTS = {
        'master': _build_db_host('', '', '', '')
    }
