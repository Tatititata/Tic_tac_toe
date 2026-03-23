from domain.model.game import GameField
from domain.constants.constants import Responce



class Service:
    _d = {'O':'X', 'X':'O'}
    


    # @staticmethod
    def winner(self, game_field:GameField):
        f = game_field
        signs = 'XO'
        sign = f[4]
        if sign in signs:
            if sign == f[0] == f[8] or sign == f[1] == f[7] or sign == f[2] == f[6] or sign == f[3] == f[5]:
                return sign
        sign = f[0]    
        if sign in signs:
            if sign == f[1] == f[2] or sign == f[3] == f[6]:
                return sign
        sign = f[8]
        if sign in signs:
            if f[6] == f[7] == sign or f[2] == f[5] == sign:
                return sign        
        if f.full():
             return -1

    # @staticmethod
    def next_move(self, f:GameField):
        best_result = -float("inf")
        best_move = None
        for i in range(f.size()):
            if f[i] == ' ':
                f.place_sign(i, 'X')
                result = self.minimax(f, 'O', -float('inf'), float("inf"))
                if result > best_result:
                    best_result = result
                    best_move = i
                del f[i]
        return best_move


    # @staticmethod
    def minimax(self, f:GameField, player, alpha, beta):
        winner = self.winner(f)
        if winner == 'X':
            return 1 + f.extra
        elif winner == 'O':
            return -1 - f.extra
        elif winner == -1:
            return 0
        
        best_result = -float("inf") if player == 'X' else float("inf")

        for i in range(f.size()):
            if f[i] == ' ':
                f.place_sign(i, player)
                result = self.minimax(f, self._d[player], alpha, beta)
                if player == 'X':
                    if result > best_result:
                        best_result = result
                    if best_result > alpha:
                        alpha = result
                    if alpha >= beta:
                        del f[i]
                        break
                else:
                    if result < best_result:
                        best_result = result
                    if result < beta:
                        beta = result
                    if beta <= alpha:
                        del f[i]
                        break
                del f[i]

        return best_result
    
    # @staticmethod
    def make_turn(self, game_field:GameField, move:str):
        if len(move) == 1 and 48 < ord(move) < 58:
            result = game_field.place_sign(ord(move) - 49, 'O')
            if result == False:
                return Responce.NOT_VALID
            winner = self.winner(game_field)
            if winner == 'O':
                return Responce.PLAYER
            elif winner == -1:
                return Responce.TIE
            game_field.place_sign(self.next_move(game_field), 'X')
            winner = self.winner(game_field)
            if winner == 'X':
                return Responce.SERVER
            elif winner == -1:
                return Responce.TIE
            return Responce.GAME


if __name__ == '__main__':
    player = 'O'
    g = GameField()
    
    while True:
        print(g)
        winner = Service.winner(g)
        if winner == -1:
            print('No winner')
            break
        elif winner == 'X':
            print('The winner is comp')
            break
        elif winner == 'O':
            print('The winner is you')
            break
        
        if player == 'O':
            pos = int(input(f'player= {player}, {list(i for i in range(g.size()) if g[i] == ' ')} > '))
            g[pos] = 'O'
        else:
            # print(f'player = {player}')
            n = Service.next_move(g)
            print(n)
            g[n] = 'X'
        player = Service._d[player]