

class GameEntity:

    def __init__(self, d:dict):
        self._id = d.get('id')
        self._field = d.get('field')
        self._player_o_id = d.get('player_o_id')
        self._player_x_id = d.get('player_x_id')
        self._winner = d.get('winner')

    def to_dict(self):
        return {
            'id': self._id,
            'field': self._field,
            'player_o_id': self._player_o_id,
            'player_x_id': self._player_x_id,
            'winner': self._winner
        }
    @property
    def id(self):
        return self._id