from web.model import WebGame
from domain import TOP, DIV, BOT
# 'lsof -i :5000\n'

class WebMapper:

    def game_to_client(self, game):
        return WebGame(game).to_dict()

    def not_valid_move_to_client(self, game, move):
        d = WebGame(game).to_dict()
        d['move'] = move
        return d 

    def game_field(self, uid, game_field, result):
        return WebGame(uid, game_field, result).to_str()
    
    def shake_hands(self):
        return  {
            "message": "Welcome to Tic-Tac-Toe API",
            "endpoints": {
                "register": {"method": "POST", "url": "/auth/register"},
                "login": {"method": "POST", "url": "/auth/login"},
                "create_game": {"method": "POST", "url": "/game"},
                "make_move": {"method": "POST", "url": "/game/{game_id}"},
                "available_games": {"method": "GET", "url": "/games/available"},
                "join_game": {"method": "POST", "url": "/game/{game_id}/join"}
                }
            }