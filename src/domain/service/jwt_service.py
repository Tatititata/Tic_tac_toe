from domain.model.jwt_request import JwtRequest
from domain.model.jwt_response import JwtResponse
from domain.model.jwt_refresh import JwtRefresh


class JwtService:
    def __init__(self, jwt_provider):
        self._provider = jwt_provider

    def login(self, data):
        if not data:
            raise ValueError('Login and password required')
        user = JwtRequest(data)
        user_id = self._provider.login(user)

        access_token = self._provider.generate_access(user_id)
        refresh_token = self._provider.generate_refresh(user_id)
        
        return JwtResponse(access_token, refresh_token)
    

    def refresh(self, data):

        refresh_token = data.get('refresh_token')
        if not refresh_token:
            raise ValueError('Refresh token required')
        
        user_refresh_token = JwtRefresh(refresh_token)

        user_id = self._provider.validate(user_refresh_token.refresh_token)
        access_token = self._provider.generate_access(user_id)
        refresh_token = self._provider.generate_refresh(user_id)

        return JwtResponse(access_token, refresh_token)

    # def validate(self, access_token):
    #     if not access_token:
    #         raise ValueError('Accessh token required')

    #     user_id = self._provider.validate(access_token)
    #     return user_id

    def validate(self, request):

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            raise ValueError("Bearer token required")

        token = auth_header.split(' ')[1]
        if not token:
            raise ValueError('Accessh token required')

        user_id = self._provider.validate(token)

        return user_id