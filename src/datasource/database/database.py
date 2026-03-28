from sqlalchemy import create_engine
from .schema import Schema



# sudo -u postgres createdb tic_tac_toe

class Database:
    _engine = None

    @classmethod
    def engine(cls):
        url = 'postgresql://postgres:5432@localhost/tic_tac_toe'
        if cls._engine is None:
            cls._engine = create_engine(url)
            Schema.init(cls._engine)
        return cls._engine