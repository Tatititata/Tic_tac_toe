from domain.model.game import Game
from datasource.mapper import GameMapper
from uuid import uuid4
from sqlalchemy import text

class Repository:
    def __init__(self, mapper:GameMapper, engine):
        self._engine = engine
        self._mapper = mapper 

    def save(self, game):
        g = self._mapper.to_entity(game)
        with self._engine.connect() as conn:
            conn.execute(text('''
            UPDATE games
            SET(field = :field, winner_id = :winner_id)
            WHERE id = :id
            '''),
            {
            'id': g.get('id'),
            'field': g.get('field'),
            'winner_id': g.get('winner_id')
            })
            conn.commit()

    def find(self, id:str):
        with self._engine.connect() as conn:
            row = conn.execute(text('''
            SELECT * FROM games
            WHERE id = :id
            '''),
            {
            'id': id
            }).fetchone()
            if row:
                return {
                    "id": row.id,
                    "field": row.field,
                    "player_x_id": row.player_x_id,
                    "player_o_id": row.player_o_id,
                    "winner": row.winner
                }
            return None


    def remove(self, game):
        pass

    def create(self, id, player_o_id, player_x_id=None):
        id = str(uuid4())
        with self._engine.connect() as conn:
            conn.execute(text('''
            INSERT INTO games(id, field, player_o_id, player_x_id, winner_id)
            VALUES(:id, :field, :player_o_id, :player_x_id, NULL)
            ''')),
            {
            'id': id,
            'field': [0] * 9,
            'player_o_id': player_o_id,
            'player_x_id': player_x_id,
            }
            conn.commit()
        return id





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