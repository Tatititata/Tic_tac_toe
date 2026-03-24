from domain.model.game_field import GameField
from datetime import datetime
class Game:

    @classmethod
    def from_dict(cls, d:dict):
        uid:str = d.get('uid')
        field:str = d.get('field')
        player_o_id:str = d.get('player_o_id')
        player_x_id:str = d.get('player_x_id')
        winner_id:str = d.get('winner_id')
        status:str = d.get('status')
        created_at:datetime = d.get('created_at')
        return cls(uid, field, player_o_id, player_x_id, winner_id, status, created_at)
    
    @classmethod
    def new(cls, uid:str, player_o_id:str, player_x_id:str = None):
        return cls(
            uid=uid,
            field=' ' * 9,
            player_o_id=player_o_id,
            player_x_id=player_x_id,
            winner_id=None,
            status='waiting' if player_o_id is None else 'in_progress',
            created_at=datetime.now()
        )

    def __init__(self, uid, field:str, player_o_id, player_x_id, winner_id, status, created_at):
        self._uid:str = uid
        self._field:GameField = GameField.from_list(field)
        self._player_o_id:str = player_o_id
        self._player_x_id:str = player_x_id
        self._winner_id:str = winner_id
        self._status = status
        self._created_at = created_at

    def to_dict(self):
        return {
            'uid': self._uid,
            'field': self._field.to_list(),
            'player_o_id': self._player_o_id,
            'player_x_id': self._player_x_id,
            'winner_id': self._winner_id,
            'status': self._status,
            'created_at': self._created_at
        }
    
    @property
    def field(self):
        return self._field