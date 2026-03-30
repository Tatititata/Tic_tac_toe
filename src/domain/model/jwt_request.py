
class JwtRequest:
    def __init__(self, data):

        self.login = data['login']
        self.password = data['password']

