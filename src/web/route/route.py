from flask import request, abort
from domain.constants.constants import *


class Route:
    def __init__(self, repo, web_mapper, service):
        self._repository = repo
        self._web_mapper = web_mapper
        self._service = service

    def shake_hands(self):
        line1 = '║ 1 ║ 2 ║ 3 ║   O = player\n'
        line2 = '║ 4 ║ 5 ║ 6 ║   X = server\n'
        line3 = '║ 7 ║ 8 ║ 9 ║\n'
        s = 'listing lsof -i :5000\n'
        s = ''
        s += 'new game: curl -X POST http://<ip address>/game\n'
        s += 'place sign: curl -X POST http://<ip address>/<game id> -d <1 to 9>\ngame field:\n'
        return s + TOP + line1 + DIV + line2 + DIV + line3 + BOT

    def create_game(self):
        id = self._repository.create()
        responce = self._web_mapper.new_game_to_client(id)
        return responce
    
    def make_move(self, id):
        move = request.get_data(as_text=True)
        game = self._repository.find(id)
        if game is None:
            abort(404, description="Game has ended or never existed")
        else:
            result = self._service.make_turn(game.field, move)
            if result == Responce.NOT_VALID:
                return self._web_mapper.not_valid_move_to_client(id, game.field, move)
            else:
                if result != Responce.GAME:
                    self._repository.remove(game)
                else:
                    self._repository.save(game)
                return self._web_mapper.game_field(id, game.field, result)

    def rep_listing(self):
        return self._repository.storage
