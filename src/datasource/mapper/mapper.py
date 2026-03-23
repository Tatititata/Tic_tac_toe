from datasource.model.model import GameEntity
from domain.model.game import Game


class GameMapper:

    def to_entity(self, game:Game):
        g = game.to_dict()
        return GameEntity(g)
    
    def to_domain(self, game:GameEntity):
        g = game.to_dict()
        return Game(g)
