from domain.constants.constants import *


class WebGame:
    def __init__(self, uid, field=None, result=None):
        self._uid = uid
        self._field = field.to_list()
        self._result = result

    def to_dict(self):
        d = {'uid': self._uid, 'field': self._field}
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
        result = 'uid: ' + self._uid + '\n' + TOP + line1 + DIV + line2 + DIV + line3 + BOT      
        if self._result == Responce.PLAYER:
            result += 'winner O\n'
        elif self._result == Responce.SERVER:
            result += 'winner X\n'
        elif self._result == Responce.TIE:
            result += 'no winner\n'
        return result