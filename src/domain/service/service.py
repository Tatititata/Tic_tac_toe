from .user_service import UserService
from .game_service import GameService
# from .auth_service import AuthService
from .jwt_service import JwtService
from .jwt_provider import JwtProvider

class Service:
    def __init__(self, repo):
        self._user_service = UserService(repo.user_repo())
        self._game_service = GameService(repo.game_repo())
        # self._auth_service = AuthService(self._user_service)
        provider = JwtProvider(self._user_service)
        self._jwt_service = JwtService(provider)

    def user_service(self):
        return self._user_service
    
    def game_service(self):
        return self._game_service
    
    # def auth_service(self):
    #     return self._auth_service
    
    def jwt_service(self):
        return self._jwt_service