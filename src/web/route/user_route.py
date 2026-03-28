from flask import request, abort
from domain import SignUpRequest, Service
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
            user = self._service.auth_service().authenticate(request.authorization)
            return self._web_mapper.user_to_client(user), 201
        except Exception as e:
            return {"error": str(e)}, 401
        
    def info(self, uid):
        try:
            self._service.auth_service().authenticate(request.authorization)
            user = self._service.user_service().find(uid)
            return self._web_mapper.user_to_client(user), 201
        except Exception as e:
            return {"error": str(e)}, 401