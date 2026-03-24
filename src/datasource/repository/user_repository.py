

from sqlalchemy import text
from datasource.model.user_model import UserModel
from datasource.mapper.user_mapper import UserMapper
from domain import User

class UserRepository:
    def __init__(self, engine, mapper:UserMapper):
        self._engine = engine
        self._mapper = mapper


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
                model = UserModel(
                uid=row.uid,
                login=row.login,
                password_hash=row.password_hash
            )
                return self._mapper.to_domain(model)
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
                model = UserModel(
                uid=row.uid,
                login=row.login,
                password_hash=row.password_hash
            )
                return self._mapper.to_domain(model)
            return None
        
    def remove(self, uid):
        pass

    def save(self, user:User):
        model = self._mapper.to_entity(user)
        with self._engine.connect() as conn:
            conn.execute(text('''
            INSERT INTO users(uid, login, password_hash)
            VALUES(:uid, :login, :password_hash)
            '''),
            model.to_dict()
            )
            conn.commit()

