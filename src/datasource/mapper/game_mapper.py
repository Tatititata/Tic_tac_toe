
from domain import Game


class GameMapper:

    @staticmethod
    def to_repo(game:Game):
        g = game.to_dict()
        return g
    
    @staticmethod
    def from_repo_to_game(row):
        return Game.from_dict(row._asdict())
    
    @staticmethod
    def lederboard_for_client(lederboard):
        return [{"player": row[0], "total": row[1], "wins": row[2], "draws": row[3]} for row in lederboard]
