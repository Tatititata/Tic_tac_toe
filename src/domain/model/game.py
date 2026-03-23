from .game_field import GameField

class Game:

    def __init__(self, d:dict):
        self._id = d.get('id')
        self._field = GameField.from_list(d.get('field', []))
        self._player_o_id = d.get('player_o_id')
        self._player_x_id = d.get('player_x_id')
        self._winner = d.get('winner')

    
    @property
    def field(self):
        return self._field

    def to_dict(self):
        return {'id': self._id, 'field': self._field.to_list()}


if __name__ == '__main__':
    pass
            

        
