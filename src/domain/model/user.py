class User:

    @classmethod
    def from_dict(cls, d:dict):
        uid = d.get('uid')
        login = d.get('login')
        password_hash = d.get('password_hash')
        return cls(uid, login, password_hash) 

    def __init__(self, uid:str, login:str, password_hash:str):
        self._uid:str = uid
        self._login:str = login
        self._password_hash:str = password_hash

    def to_dict(self):
        return {
                "uid": self._uid,
                "login": self._login,
                "password_hash": self._password_hash
                }
