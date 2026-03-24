from .game_repository import GameRepository
from .user_repository import UserRepository
from datasource.mapper import Mapper


class Repository:

    def __init__(self, engine, mapper:Mapper):
        self._user_repo = UserRepository(engine, mapper.user_mapper())
        self._game_repo = GameRepository(engine, mapper.game_mapper())
        

    def user_repo(self):
        return self._user_repo
    
    def game_repo(self):
        return self._game_repo

