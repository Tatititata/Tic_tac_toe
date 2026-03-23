

class GameEntity:

    def __init__(self, id, data):
        self._id = id
        self._data = data

    def to_dict(self):
        return {'id': self._id, 'field': [d for d in self._data]}

    @property
    def id(self):
        return self._id