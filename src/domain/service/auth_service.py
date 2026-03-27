from domain.model.signup_request import SignUpRequest

class AuthService:
    def __init__(self, user_service):
        self._service = user_service

    def register(self, signup:SignUpRequest):
        return self._service.register(signup.login, signup.password)
    
    def authenticate(self, login, password):
        return self._service.login(login, password)