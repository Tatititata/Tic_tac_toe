from .game_field import GameField

class Game:

    @classmethod
    def from_dict(cls, d:dict):
        field = GameField.from_list(d.get('field', []))
        return cls(d.get('id'), field)

    def __init__(self, id, field:GameField=None):
        self._id = id
        self._field = field if field else GameField()
    
    @property
    def field(self):
        return self._field

    def to_dict(self):
        return {'id': self._id, 'field': self._field.to_list()}


if __name__ == '__main__':
    pass
            

        
