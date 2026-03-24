from domain.model import User
from uuid import uuid4
from hashlib import sha256

class UserService:
    def __init__(self, user_repo):
        self._user_repo = user_repo

    def register(self, login, password):
        uid = str(uuid4())
        password_hash = sha256(password.encode()).hexdigest()
        user = User(uid, login, password_hash)
        self._user_repo.save(user)
        return uid