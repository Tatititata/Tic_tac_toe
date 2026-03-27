


class WebGame:
    def __init__(self, game):
        game = game.to_dict()
        self._uid = game.get('uid')
        self._field = game.get('field')
        self._status = game.get('status')
        self._winner_id = game.get('winner_id')

    def to_dict(self):
        return {
            'uid': self._uid, 
            'field': self._field, 
            'status': self._status, 
            'winner_id': self._winner_id}

