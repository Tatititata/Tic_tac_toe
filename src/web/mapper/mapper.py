from ..model import *


class WebMapper:
    # def new_game_to_client(self, id):
    #     return NewGame(id).to_dict()
    

    # def not_valid_move_to_client(self, id, game_field, move):
    #     d = OldGame(id, game_field).to_dict()
    #     d['error'] = 'Invalid move ' + move
    #     return d

    # def game_field(self, id, game_field, result):
    #     return OldGame(id, game_field, result).to_dict()
    


    def new_game_to_client(self, id):
        return NewGame(id).to_str()
    

    def not_valid_move_to_client(self, id, game_field, move):
        d = OldGame(id, game_field).to_str()
        return d + 'Invalid move ' + move + '\n'

    def game_field(self, id, game_field, result):
        return OldGame(id, game_field, result).to_str()