from domain import Game
from datasource.mapper import GameMapper
from sqlalchemy import text

class GameRepository:
    def __init__(self, mapper:GameMapper, engine):
        self._engine = engine
        self._mapper = mapper 

    def save(self, game:Game):
        game_dict = self._mapper.to_repo(game)
        with self._engine.connect() as conn:
            conn.execute(text('''
            UPDATE games
            SET(field = :field, winner_id = :winner_id, status = :status)
            WHERE uid = :uid
            '''),
            game_dict
            )
            conn.commit()

    def find(self, uid:str):
        with self._engine.connect() as conn:
            row = conn.execute(text('''
            SELECT * FROM games
            WHERE uid = :uid
            '''),
            {
            'uid': uid
            }).fetchone()
            if row:
                game = self._mapper.from_repo_to_game(row)
                return game
            return None


    def remove(self, game):
        pass

    def register(self, game:Game):
        with self._engine.connect() as conn:
            conn.execute(text('''
            INSERT INTO games(uid, field, player_o_id, player_x_id, winner_id, status, created_at)
            VALUES(:uid, :field, :player_o_id, :player_x_id, :winner_id, :status, :created_at)
            ''')),
            {
                game.to_dict()
            }
            conn.commit()
        return 

