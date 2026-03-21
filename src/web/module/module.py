from flask import Flask

from ..route import Route

class Module:
    def __init__(self, repository, web_mapper, service):
        route = Route(repository, web_mapper, service)
        self._app = Flask(__name__)
        self._app.add_url_rule('/', 'hello', route.shake_hands, methods=['GET'])
        self._app.add_url_rule('/game', 'create_game', route.create_game, methods=['POST'])
        self._app.add_url_rule('/<id>', 'make_move', route.make_move, methods=['POST'])
        self._app.add_url_rule('/r', 'check_repository', route.rep_listing, methods=['POST'])

    def run(self):
        self._app.run()


if __name__ == '__main__':
    pass