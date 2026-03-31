
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
    def leaderboard_for_client(leaderboard):
        return [{"player": row[0], "ratio": row[1] } for row in leaderboard]
