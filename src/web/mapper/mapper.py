from web.model import WebGame
from domain import JwtResponse
# from domain import TOP, DIV, BOT
# 'lsof -i :5000\n'

class WebMapper:

    @staticmethod
    def game_to_client(game):
        return WebGame(game).to_dict()


    @staticmethod
    def not_valid_move_to_client(game, move):
        d = WebGame(game).to_dict()
        d['move'] = move
        return d 
    
    @staticmethod  
    def shake_hands(self):
        return  {
            "message": "Welcome to Tic-Tac-Toe API",
            "endpoints": {
                "register": {"method": "POST", "url": "/auth/register"},
                "login": {"method": "POST", "url": "/auth/login"},
                "create_game": {"method": "POST", "url": "/game"},
                "make_move": {"method": "POST", "url": "/{game_id}"},
                "available_games": {"method": "GET", "url": "/games/available"},
                "join_game": {"method": "POST", "url": "/{game_id}/join"}
                }
            }
    

    @staticmethod    
    def user_to_client(user):
        user = user.to_dict()
        return {
            'uid': user['uid'],
            'login': user['login']
        }
    
    @staticmethod
    def tokens_to_client(responce:JwtResponse):
        return responce.to_dict()
    
    @staticmethod
    def self_to_client(uid):
        return {
            'uid': uid,
        }