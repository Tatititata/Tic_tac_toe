from domain.model.model import Game
from ..mapper import GameMapper
from uuid import uuid4

class Repository:
    def __init__(self):
        self._storage = {}
        self._mapper = GameMapper()

    def save(self, game:Game):
        g = self._mapper.to_entity(game)
        self._storage[g.id] = g

    def find(self, id:str):
        g = self._storage.get(id)
        if g:
            return self._mapper.to_domain(g)

    def remove(self, game:Game):
        g = self._mapper.to_entity(game)
        id = g.id
        if id in self._storage:
            del self._storage[id]

    def create(self):
        id = str(uuid4())
        # id = '1'
        self._storage[id] = self._mapper.to_entity(Game(id))
        return id

    @property
    def storage(self):
        return [v.to_dict() for v in self._storage.values()]