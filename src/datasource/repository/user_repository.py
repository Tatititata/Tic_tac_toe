from sqlalchemy import text
from datasource.mapper.user_mapper import UserMapper
from domain import User

class UserRepository:
    def __init__(self, engine, mapper:UserMapper):
        self._engine = engine
        self._user_mapper = mapper


    def find_by_id(self, uid:str):
        with self._engine.connect() as conn:
            row = conn.execute(text('''
            SELECT * FROM users
            WHERE uid = :uid
            '''),
            {
            'uid': uid
            }).fetchone()
            if row:
                return self._user_mapper.from_repo_to_user(row)
            return None

    def find_by_login(self, login:str):
        with self._engine.connect() as conn:
            row = conn.execute(text('''
            SELECT * FROM users
            WHERE login = :login
            '''),
            {
            'login': login
            }).fetchone()
            if row:
                return self._user_mapper.from_repo_to_user(row)
            return None
        
    def remove(self, uid):
        pass

    def save(self, user:User):
        with self._engine.connect() as conn:
            conn.execute(text('''
            INSERT INTO users(uid, login, password_hash)
            VALUES(:uid, :login, :password_hash)
            '''),
            self._user_mapper.to_repo(user)
            )
            conn.commit()

