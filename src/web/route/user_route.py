from flask import request, abort
from domain import SignUpRequest, Service
from datasource import Repository
from web.mapper.mapper import WebMapper

class UserRoute:
    def __init__(self, repo:Repository, web_mapper:WebMapper, service:Service):
        self._repo = repo
        self._web_mapper = web_mapper
        self._service = service

    def register(self):
        data = request.get_json()
        if not data:
            return {"error": "login and password required"}, 400
        login = data.get('login')
        password = data.get('password')

        signup = SignUpRequest(login, password)
        try:
            user_id = self._service.auth_service().register(signup)
            return {"id": user_id}, 201
        except Exception as e:
            return {"error": str(e)}, 400
        
    def login(self):
        try:
            auth = request.authorization
            if not auth:
                raise ValueError('Authorization header required')
            user_id = self._service.auth_service().authenticate(auth.username, auth.password)
            return {"id": user_id}
        except Exception as e:
            return {"error": str(e)}, 401
        
    