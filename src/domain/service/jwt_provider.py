from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import decode_token


class JwtProvider:
    def __init__(self, user_service):
        self._user_service = user_service

    def login(self, user):
        user = self._user_service.login(user.login, user.password)
        if not user:
            raise ValueError("Invalid credentials")
        return user.uid

    def generate_access(self, user_id):
        return create_access_token(identity=user_id)

    def generate_refresh(self, user_id):
        return create_refresh_token(identity=user_id)
        
    def validate(self, token):
        try:
            decoded = decode_token(token)
            user_id = decoded.get("sub")
            self._user_service.find(user_id)
            return user_id
        except Exception:
            raise ValueError("Invalid or expired token")