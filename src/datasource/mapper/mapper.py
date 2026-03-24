from .game_mapper import GameMapper
from .user_mapper import UserMapper

class Mapper:
    def __init__(self):
        self._user_mapper = UserMapper()
        self._game_mapper = GameMapper()

    def user_mapper(self):
        return self._user_mapper
    
    def game_mapper(self):
        return self._game_mapper