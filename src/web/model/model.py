from domain.constants.constants import *

class NewGame:
    def __init__(self, id):
        self._id = id

    def to_dict(self):
        return {'id': self._id}

    def to_str(self):      
        line = f'║   ║   ║   ║\n'
        return 'id: ' + self._id + '\n' + TOP + line + DIV + line + DIV + line + BOT      


class OldGame:
    def __init__(self, id, field, result=None):
        self._id = id
        self._field = field.to_list()
        self._result = result

    def to_dict(self):
        d = {'id': self._id, 'field': self._field}
        if self._result == Responce.PLAYER:
            d['winner'] = 'O'
        elif self._result == Responce.SERVER:
            d['winner'] = 'X'
        return d

    def to_str(self):
        f = self._field         
        line1 = f'║ {f[0]} ║ {f[1]} ║ {f[2]} ║\n'
        line2 = f'║ {f[3]} ║ {f[4]} ║ {f[5]} ║\n'
        line3 = f'║ {f[6]} ║ {f[7]} ║ {f[8]} ║\n'
        result = 'id: ' + self._id + '\n' + TOP + line1 + DIV + line2 + DIV + line3 + BOT      
        if self._result == Responce.PLAYER:
            result += 'winner O\n'
        elif self._result == Responce.SERVER:
            result += 'winner X\n'
        elif self._result == Responce.TIE:
            result += 'no winner\n'
        return result