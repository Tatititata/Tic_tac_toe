from flask import request
from domain import Service
from web.mapper.mapper import WebMapper

class UserRoute:
    def __init__(self, web_mapper:WebMapper, service:Service):
        self._web_mapper = web_mapper
        self._service = service

    def register(self):
        data = request.get_json()
        if not data:
            return {"error": "login and password required"}, 400
        login = data.get('login')
        password = data.get('password')
        try:
            user = self._service.user_service().register(login, password)
            return self._web_mapper.user_to_client(user), 201
        except Exception as e:
            return {"error": str(e)}, 400
        
    def login(self):
        try:
            data = request.get_json()
            user_tokens = self._service.jwt_service().login(data)
            return self._web_mapper.tokens_to_client(user_tokens), 201
        except Exception as e:
            return {"error": str(e)}, 401
        
    def refresh(self):
        try:
            user_tokens = self._service.jwt_service().refresh(request.get_json())
            return self._web_mapper.tokens_to_client(user_tokens), 201
        except Exception as e:
            return {"error": str(e)}, 401
        
    def info(self, uid):
        try:
            self._service.jwt_service().validate(request)
            user = self._service.user_service().find(uid)
            return self._web_mapper.user_to_client(user), 200
        except Exception as e:
            return {"error": str(e)}, 401
    
    def me(self):
        try:
            uid = self._service.jwt_service().validate(request)
            return self._web_mapper.self_to_client(uid), 200
        except Exception as e:
            return {"error": str(e)}, 401

