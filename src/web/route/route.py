from flask import request, abort
from domain.constants.constants import Responce
from web.mapper import WebMapper


class Route:
    def __init__(self, repo, web_mapper:WebMapper, service):
        self._user_repo = repo.user_repo()
        self._game_repo = repo.game_repo()
        self._web_mapper = web_mapper
        self._service = service





    def shake_hands(self):
        return self._web_mapper.shake_hands()

    def create_game(self):
        uid = self._repository.create()
        responce = self._web_mapper.new_game_to_client(uid)
        return responce
    
    def make_move(self, uid):
        move = request.get_data(as_text=True)
        game = self._repository.find(uid)
        if game is None:
            abort(404, description="Game has ended or never existed")
        else:
            result = self._service.make_turn(game.field, move)
            if result == Responce.NOT_VALID:
                return self._web_mapper.not_valid_move_to_client(uid, game.field, move)
            else:
                if result != Responce.GAME:
                    self._repository.remove(game)
                else:
                    self._repository.save(game)
                return self._web_mapper.game_field(uid, game.field, result)

    def rep_listing(self):
        return self._repository.storage
