class Module:

    def __init__(self, app, route):
        self._app = app
        self._route = route

    def register(self):

        self._app.add_url_rule('/', 'hello', self._route.shake_hands, methods=['GET'])
        self._app.add_url_rule('/game', 'create_game', self._route.create_game, methods=['POST'])
        self._app.add_url_rule('/<uid>', 'make_move', self._route.make_move, methods=['POST'])
        self._app.add_url_rule('/r', 'check_repository', self._route.rep_listing, methods=['POST'])


if __name__ == '__main__':
    pass