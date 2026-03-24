from domain.model.game import GameModel
from domain import Game


class GameMapper:

    def to_repo(self, game:Game):
        g = game.to_dict()
        return g
    
    def from_repo_to_game(self, row):
        return Game.from_dict(row._asdict())
