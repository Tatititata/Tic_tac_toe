from flask import request, make_response, jsonify
from domain import Service
from web.mapper.mapper import WebMapper

class GameRoute:

    def __init__(self, web_mapper:WebMapper, service:Service):
        self._web_mapper = web_mapper
        self._service = service

    def shake_hands(self):
        return self._web_mapper.shake_hands()

    def create_game(self):
        try:
            uid = self._service.jwt_service().validate(request)
            data = request.get_json()
            game = self._service.game_service().create(player_o_id=uid, player_x_id=data.get('type', 'bot'))
            data = self._web_mapper.game_to_client(game)
            return make_response(jsonify(data), 201)
        except Exception as e:
            return {"error": str(e)}, 401
        

    def make_move(self, game_id):
        try:
            uid = self._service.jwt_service().validate(request)
            data = request.get_json()
            move = data.get('move')
            game = self._service.game_service().make_move(game_id, uid, move)
            data = self._web_mapper.game_to_client(game)
            return make_response(jsonify(data), 200)
        except Exception as e:
            return {"error": str(e)}, 401

    def join(self, game_id):
        try:
            uid = self._service.jwt_service().validate(request)
            game = self._service.game_service().join(game_id, uid)
            data = self._web_mapper.game_to_client(game)
            return make_response(jsonify(data), 200)
        except Exception as e:
            return {"error": str(e)}, 401
        
    
    def get_games_for_user(self):
        try:
            uid = self._service.jwt_service().validate(request)
            games = self._service.game_service().get_games_for_user(uid)
            data = [self._web_mapper.game_to_client(game) for game in games]
            return make_response(jsonify(data), 200)
        except Exception as e:
            return {"error": str(e)}, 401
        
    def get_history(self):
        try:
            uid = self._service.jwt_service().validate(request)
            games = self._service.game_service().get_history(uid)
            data = [self._web_mapper.game_to_client(game) for game in games]
            return make_response(jsonify(data), 200)
        except Exception as e:
            return {"error": str(e)}, 401
        
    def leaderboard(self):
        try:
            self._service.jwt_service().validate(request)
            data = request.get_json()
            limit = data.get('limit')
            leaderboard = self._service.game_service().get_leaderboard(limit)
            return make_response(jsonify(leaderboard), 200)
        except Exception as e:
            return {"error": str(e)}, 401