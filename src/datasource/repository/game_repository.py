from domain import Game
from sqlalchemy import text

class GameRepository:
    def __init__(self, engine, mapper):
        self._engine = engine
        self._mapper = mapper 

    def save_move(self, game:Game):
        game_dict = self._mapper.to_repo(game)
        with self._engine.connect() as conn:
            conn.execute(text('''
            UPDATE games
            SET field = :field, winner_id = :winner_id, status = :status 
            WHERE uid = :uid
            '''),
            game_dict
            )
            conn.commit()

    def save_x_player(self, game:Game):
        game_dict = self._mapper.to_repo(game)
        with self._engine.connect() as conn:
            conn.execute(text('''
            UPDATE games
            SET player_x_id = :player_x_id, status = :status 
            WHERE uid = :uid
            '''),
            game_dict
            )
            conn.commit()

    def find(self, game_id:str):
        with self._engine.connect() as conn:
            row = conn.execute(text('''
            SELECT * FROM games
            WHERE uid = :uid
            '''),
            {
            'uid': game_id
            }).fetchone()
            if row:
                return self._mapper.from_repo_to_game(row)
            return None


    def remove(self, game):
        pass

    def register(self, game:Game):
        with self._engine.connect() as conn:
            conn.execute(text('''
            INSERT INTO games(uid, field, player_o_id, player_x_id, winner_id, status, created_at)
            VALUES(:uid, :field, :player_o_id, :player_x_id, :winner_id, :status, :created_at)
            '''),
                game.to_dict()
            )
            conn.commit()
        return 

    def get_games_for_user(self, user_id):
        with self._engine.connect() as conn:
            rows = conn.execute(text('''
            SELECT * FROM games
            WHERE status != 'finished' 
            AND (player_o_id = :user_id OR  player_x_id = :user_id OR
            (player_o_id != :user_id AND player_x_id IS NULL)
            )
            '''),
            {
            'user_id': user_id
            }).fetchall()
            if rows:
                return [self._mapper.from_repo_to_game(row) for row in rows]
            return []
        
    def get_history(self, user_id):
        with self._engine.connect() as conn:
            rows = conn.execute(text('''
            SELECT * FROM games
            WHERE status = 'finished' 
            AND (player_o_id = :user_id OR  player_x_id = :user_id)
            '''),
            {
            'user_id': user_id
            }).fetchall()
            if rows:
                return [self._mapper.from_repo_to_game(row) for row in rows]
            return []
        
    def get_history(self, limit):
        with self._engine.connect() as conn:
            rows = conn.execute(text('''
            select player, 
                case 
                    when (loss + tie) = 0 then 999999
                    else win::float / (loss + tie)
                end as ratio
            from

            (select ft.player, 
            sum (case when player = winner_id then 1 else 0 end) as win,
            sum (case when (player != winner_id and winner_id is not null) then 1 else 0 end) as loss,
            sum (case when winner_id is null then 1 else 0 end) as tie

            from
            (select player_o_id as player, winner_id from games
            where status = 'finished'
            union all
            select player_x_id as player, winner_id from games
            where status = 'finished') as ft

            group by player)

            order by ratio desc
            limit :limit
            '''),
            {
            'limit': limit
            }).fetchall()
            if rows:
                return rows
            return []