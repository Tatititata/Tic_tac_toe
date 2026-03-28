from uuid import uuid4
from domain.model import Game, GameLogic
from domain.exeptions import GameError

class GameService:
    def __init__(self, game_repo):
        self._game_repo = game_repo

    def create(self, player_o_id, player_x_id):
        if player_x_id == 'human':
            player_x_id = None
        game_id = str(uuid4())
        game = Game.new(
            game_id=game_id, 
            player_o_id=player_o_id,
            player_x_id=player_x_id
        )
        self._game_repo.register(game)
        return game
    
    def make_move(self, game_id, uid, move):
        game = self._game_repo.find(game_id)

        if not game:
            raise GameError.NotFound()
        
        if game.status == 'finished':
            raise GameError.Finished()
        if game.status == 'waiting':
            raise GameError.NotInProgress()
        
        pl_o, pl_x = game.players_OX
        o, x =  game.field.quantity_OX

        if uid == pl_x:
            if o != x + 1:
                raise GameError.InvalidMove('You are X player. It\'s player O turn now.')
            elif not game.field.place_sign(move - 1, 'X'):
                raise GameError.InvalidMove()
        elif uid == pl_o:
            if o != x:
                raise GameError.InvalidMove('You are O player. It\'s player X turn now.')
            elif not game.field.place_sign(move - 1, 'O'):
                raise GameError.InvalidMove()
        else:
            raise GameError.InvalidMove(f'Player is not valid')
        
        self._check_winner(game)

        if game.status != 'finished' and pl_x == 'bot':
            move = GameLogic.next_move(game.field)
            game.field.place_sign(move, 'X')
            self._check_winner(game)

        self._game_repo.save_move(game)
        return game
    
    def _check_winner(self, game):
        winner = GameLogic.winner(game.field)
        if winner:
                game.set_winner(winner)
        elif game.field.full():
            game.finish()

    def join(self, game_id, player_id):
        game = self._game_repo.find(game_id)
        if not game:
            raise GameError.NotFound()
        
        if game.status == 'finished':
            raise GameError.Finished()
        
        pl_o, pl_x = game.players_OX
        
        if pl_x is None and player_id != pl_o:
            game.set_x_player(player_id)
            self._game_repo.save_x_player(game)
        return game
    
    def get_games_for_user(self, user_id):
        games = self._game_repo.get_games_for_user(user_id)
        return games