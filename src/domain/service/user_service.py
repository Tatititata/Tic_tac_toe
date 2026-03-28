from domain.model import User
from uuid import uuid4
from hashlib import sha256

class UserService:
    def __init__(self, user_repo):
        self._user_repo = user_repo

    def register(self, login, password):
        user = self._user_repo.find_by_login(login)
        if user:
            raise ValueError('User already exists')
        uid = str(uuid4())
        password_hash = sha256(password.encode()).hexdigest()
        user = User(uid, login, password_hash)
        self._user_repo.save(user)
        return user
    
    def login(self, login, password):
        user = self._user_repo.find_by_login(login)
        if not user:
            raise ValueError('User not found')  
        
        password_hash = sha256(password.encode()).hexdigest()
        if user.password_hash != password_hash:
            raise ValueError('Invalid password')  
        
        return user
    
    def find(self, uid):
        user = self._user_repo.find_by_id(uid)
        if user is None:
            raise ValueError('User not found')  
        return user