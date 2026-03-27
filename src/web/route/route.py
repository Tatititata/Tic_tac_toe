from .game_route import GameRoute
from .user_route import UserRoute
from datasource import Repository
from domain import Service

class Route:
    def __init__(self, repo:Repository, web_mapper, service:Service):
        self._user_route = UserRoute(repo, web_mapper, service)
        self._game_route = GameRoute(repo, web_mapper, service)

    def user_route(self):
        return self._user_route
    
    def game_route(self):
        return self._game_route
    
