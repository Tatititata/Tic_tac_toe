class Module:

    def __init__(self, app, route):
        self._app = app
        self._game_route = route.game_route()
        self._user_route = route.user_route()

    def register(self):

        self._app.add_url_rule('/', 'hello', self._game_route.shake_hands, methods=['GET'])
        self._app.add_url_rule('/games/available', 'available', self._game_route.get_games_for_user, methods=['GET'])
        self._app.add_url_rule('/game', 'create_game', self._game_route.create_game, methods=['POST'])
        self._app.add_url_rule('/<game_id>', 'make_move', self._game_route.make_move, methods=['POST'])
        self._app.add_url_rule('/<game_id>/join', 'join', self._game_route.join, methods=['POST'])
        # self._app.add_url_rule('/r', 'check_repository', self._game_route.rep_listing, methods=['POST'])
        self._app.add_url_rule('/auth/register', 'register', self._user_route.register, methods=['POST'])
        self._app.add_url_rule('/auth/login', 'login', self._user_route.login, methods=['POST'])


if __name__ == '__main__':
    pass