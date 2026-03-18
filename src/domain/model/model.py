class GameField:

    _players = (False, True)

    def __init__(self):
        self.field = [None] * 9

    def winner(self):
        f = self.field
        if f[4] in self._players:
            if f[0] == f[4] == f[8] or f[1] == f[4] == f[7] or f[2] == f[4] == f[6] or f[3] == f[4] == f[5]:
                return f[4]
        if f[0] in self._players:
            if f[0] == f[1] == f[2] or f[0] == f[3] == f[6]:
                return f[0]
        if f[8] in self._players:
            if f[6] == f[7] == f[8] or f[2] == f[5] == f[8]:
                return f[8]        
        if all(map(lambda x: x is not None, f)):
             return -1
        
    def place_sign(self, pos, sign):
        if 0 <= pos < len(self.field) and self.field[pos] is None and sign in (True, False):
            self.field[pos] = sign
        else:
            raise

    def remove_sign(self, pos):
        if 0 <= pos < len(self.field):
            self.field[pos] = None
    
    @property
    def extra(self):
        return sum(1 for i in self.field if i is None)
              
    
    def __str__(self):
        d = {True: 'X', False: 'O'}
        f = self.field         
        top = '╔═══╦═══╦═══╗\n'
        div = '╠═══╬═══╬═══╣\n'
        bot = '╚═══╩═══╩═══╝'
        line1 = f'║ {d.get(f[0], ' ')} ║ {d.get(f[1], ' ')} ║ {d.get(f[2], ' ')} ║\n'
        line2 = f'║ {d.get(f[3], ' ')} ║ {d.get(f[4], ' ')} ║ {d.get(f[5], ' ')} ║\n'
        line3 = f'║ {d.get(f[6], ' ')} ║ {d.get(f[7], ' ')} ║ {d.get(f[8], ' ')} ║\n'
        return  top + line1 + div + line2 + div + line3 + bot



class Model:

    @staticmethod
    def next_move(g:GameField):
        best_result = -float("inf")
        best_move = None
        for i in range(len(g.field)):
            if g.field[i] is None:
                g.place_sign(i, True)
                result = Model.minimax(g, False, -float('inf'), float("inf"))
                if result > best_result:
                    best_result = result
                    best_move = i
                g.remove_sign(i)
        return best_move


    @staticmethod
    def minimax(g:GameField, player:bool, alpha, beta):
        
        winner = g.winner()
        if winner == True:
            return 1 + g.extra
        elif winner == False:
            return -1 - g.extra
        elif winner == -1:
            return 0
        
        best_result = -float("inf") if player else float("inf")

        for i in range(len(g.field)):
            if g.field[i] is None:
                g.place_sign(i, player)
                result = Model.minimax(g, not player, alpha, beta)
                if player == True:
                    if result > best_result:
                        best_result = result
                    if best_result > alpha:
                        alpha = result
                    if alpha >= beta:
                        g.remove_sign(i)
                        break
                else:
                    if result < best_result:
                        best_result = result
                    if result < beta:
                        beta = result
                    if beta <= alpha:
                        g.remove_sign(i)
                        break
                g.remove_sign(i)

        return best_result

         
         
    

if __name__ == '__main__':
    player = True
    g = GameField()
    
    while True:
        print(g)
        winner = g.winner()
        if winner == -1:
            print('No winner')
            break
        elif winner == True:
            print('The winner is comp')
            break
        elif winner == False:
            print('The winner is you')
            break
        
        if player:
            pos = int(input(f'player= {player}, {list(i for i in range(len(g.field)) if g.field[i] is None)} > '))
            g.place_sign(pos, False)
        else:
            # print(f'player = {player}')
            n = Model.next_move(g)
            print(n)
            g.place_sign(n, True)
        player = not player
            

        
