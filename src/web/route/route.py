from .game_route import GameRoute
from .user_route import UserRoute


class Route:
    def __init__(self, web_mapper, service):
        self._user_route = UserRoute(web_mapper, service)
        self._game_route = GameRoute(web_mapper, service)

    def user_route(self):
        return self._user_route
    
    def game_route(self):
        return self._game_route
    
