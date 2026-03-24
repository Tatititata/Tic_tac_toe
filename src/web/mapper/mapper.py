from web.model import WebGame


class WebMapper:
    # def new_game_to_client(self, uid):
    #     return NewGame(uid).to_dict()
    

    # def not_valid_move_to_client(self, uid, game_field, move):
    #     d = OldGame(uid, game_field).to_dict()
    #     d['error'] = 'Invalid move ' + move
    #     return d

    # def game_field(self, uid, game_field, result):
    #     return OldGame(uid, game_field, result).to_dict()
    


    def new_game_to_client(self, uid):
        return WebGame(uid).to_str()
    

    def not_valid_move_to_client(self, uid, game_field, move):
        d = WebGame(uid, game_field).to_str()
        return d + 'Invalid move ' + move + '\n'

    def game_field(self, uid, game_field, result):
        return WebGame(uid, game_field, result).to_str()
    
    def shake_hands(self):
        line1 = '║ 1 ║ 2 ║ 3 ║   O = player\n'
        line2 = '║ 4 ║ 5 ║ 6 ║   X = server\n'
        line3 = '║ 7 ║ 8 ║ 9 ║\n'
        s = 'listing lsof -i :5000\n'
        s = ''
        s += 'new game: curl -X POST http://<ip address>/game\n'
        s += 'place sign: curl -X POST http://<ip address>/<game uid> -d <1 to 9>\ngame field:\n'
        return s + TOP + line1 + DIV + line2 + DIV + line3 + BOT