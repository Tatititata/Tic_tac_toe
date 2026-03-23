from domain.constants.constants import TOP, DIV, BOT

class GameField:

    @classmethod
    def from_list(cls, l:list):
        obj = cls()
        for i, sign in enumerate(l):
            if sign != ' ':
                obj.place_sign(i, sign)
        return obj

    def __init__(self):
        self._field = [' '] * 9

    def size(self):
        return len(self._field)
    
    def __getitem__(self, pos):
        if 0 <= pos < len(self._field):
            return self._field[pos]

    def place_sign(self, pos, sign):
        if 0 <= pos < len(self._field) and self._field[pos] == ' ' and sign in 'XO':
            self._field[pos] = sign
            return True
        else:
            return False

    def __delitem__(self, pos):
        if 0 <= pos < len(self._field):
            self._field[pos] = ' '
    
    @property
    def extra(self):
        return sum(1 for i in self._field if i is None)
              
    def full(self):
        return all(map(lambda x: x != ' ', self._field))



    def __str__(self):
        f = self._field         
        line1 = f'║ {f[0]} ║ {f[1]} ║ {f[2]} ║\n'
        line2 = f'║ {f[3]} ║ {f[4]} ║ {f[5]} ║\n'
        line3 = f'║ {f[6]} ║ {f[7]} ║ {f[8]} ║\n'
        return  TOP + line1 + DIV + line2 + DIV + line3 + BOT


    def to_list(self):
        return [i for i in self._field]


if __name__ == '__main__':
    pass
            

        
