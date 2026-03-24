from uuid import uuid4
from domain.model import Game

class GameService:
    def __init__(self, game_repo):
        self._user_repo = game_repo

    def create(self, player_o_id, player_x_id):
        uid = str(uuid4())
        game = Game.new(
            uid=uid, 
            player_o_id=player_o_id,
            player_x_id=player_x_id
        )


        return uid