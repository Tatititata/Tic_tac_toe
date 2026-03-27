from domain.model.game_field import GameField
from domain.constants import Responce



class GameLogic:
    _d = {'O':'X', 'X':'O'}
    
    @staticmethod
    def winner(game_field:GameField):
        f = game_field 
        if f[4] != ' ':
            if f[4] == f[0] == f[8] or f[4] == f[1] == f[7] or f[4] == f[2] == f[6] or f[4] == f[3] == f[5]:
                return f[4]
        if f[0] != ' ':
            if f[0] == f[1] == f[2] or f[0] == f[3] == f[6]:
                return f[0]
        if f[8] != ' ':
            if f[6] == f[7] == f[8] or f[2] == f[5] == f[8]:
                return f[8]        
        return False

    @staticmethod
    def next_move(f:GameField):
        best_result = -float("inf")
        best_move = None
        for i in range(f.size()):
        # for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            if f[i] == ' ':
                f.place_sign(i, 'X')
                # input(f)
                result = GameLogic.minimax(f, 'O', -float('inf'), float("inf"))
                if result > best_result:
                    best_result = result
                    best_move = i
                del f[i]
        return best_move


    @staticmethod
    def minimax(f:GameField, player, alpha, beta):
        winner = GameLogic.winner(f)
        if winner:
            if winner == 'X':
                return 1 + f.extra
            if winner == 'O':
                return -1 - f.extra 
        if f.full():
            return 0
        
        best_result = -float("inf") if player == 'X' else float("inf")

        for i in range(f.size()):
            if f[i] == ' ':
                f.place_sign(i, player)
                # input(f)
                # winner = GameLogic.winner(f, player)
                # if winner:
                #     print(winner, end=' ')
                    
                #     if player == 'X':
                #         print(1 + f.extra)
                #         del f[i]
                #         return 1 + f.extra
                #     if player == 'O':
                #         print(-1 - f.extra)
                #         del f[i]
                #         return -1 - f.extra 
                # if f.full():
                #     print(0)
                #     del f[i]
                #     return 0
                result = GameLogic.minimax(f, GameLogic._d[player], alpha, beta)
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
    # def make_turn(self, game_field:GameField, move:int):
    #     if 0 < move < 10:
    #         result = game_field.place_sign(move, 'O')
    #         if result == False:
    #             return Responce.NOT_VALID
    #         winner = self.winner(game_field)
    #         if winner == 'O':
    #             return Responce.PLAYER
    #         elif winner == -1:
    #             return Responce.TIE
    #         game_field.place_sign(self.next_move(game_field), 'X')
    #         winner = self.winner(game_field)
    #         if winner == 'X':
    #             return Responce.SERVER
    #         elif winner == -1:
    #             return Responce.TIE
    #         return Responce.IN_PROGRESS


if __name__ == '__main__':
    player = 'O'
    g = GameField()
    print(g)
    while True:
        winner = GameLogic.winner(g)
        print(winner)
        if winner == 'X':
            print('The winner is comp')
            break
        elif winner == 'O':
            print('The winner is you')
            break
        elif g.full():
            print('No winner')
            break

        if player == 'O':
            pos = int(input(f'player= {player}, {list(i + 1 for i in range(g.size()) if g[i] == ' ')} > '))
            g.place_sign(pos - 1,'O')
        else:
            # print(f'player = {player}')
            n = GameLogic.next_move(g)
            print(n + 1)
            g.place_sign(n, 'X')
        print(g)

        player = GameLogic._d[player]