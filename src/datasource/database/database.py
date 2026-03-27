from sqlalchemy import create_engine



# sudo -u postgres createdb tic_tac_toe

class Database:
    _engine = None

    @classmethod
    def engine(cls):
        url = 'postgresql://postgres:5432@localhost/tic_tac_toe'
        if cls._engine is None:
            cls._engine = create_engine(url)
        return cls._engine