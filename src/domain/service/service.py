from .user_service import UserService
from .game_service import GameService
from .auth_service import AuthService

class Service:
    def __init__(self, repo):
        self._user_service = UserService(repo.user_repo())
        self._game_service = GameService(repo.game_repo())
        self._auth_service = AuthService(self._user_service)

    def user_service(self):
        return self._user_service
    
    def game_service(self):
        return self._game_service
    
    def auth_service(self):
        return self._auth_service