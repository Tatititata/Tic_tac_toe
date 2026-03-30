

class JwtResponse:
    def __init__(self, access, refresh):
        self._access_token = access
        self._refresh_token = refresh


    def to_dict(self):
        return {
            'access_token': self._access_token,
            'refresh_token': self._refresh_token
        }


