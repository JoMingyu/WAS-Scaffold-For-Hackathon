from contextlib import contextmanager
from functools import wraps

from sqlalchemy.orm import sessionmaker

from app.extensions import db_master_engine


@contextmanager
def _session_scope(engine):
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def wrap_session(engine=None):
    if engine is None:
        engine = db_master_engine

    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            with _session_scope(engine) as session:
                result = fn(self, session, *args, **kwargs)

                if hasattr(result, '_sa_instance_state'):
                    session.expunge(result)

                return result
        return wrapper
    return decorator
