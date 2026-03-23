from datasource import Repository, GameMapper
from domain import Service
from web import WebMapper, Module, Route
from flask import Flask




class Container:
    _app: Flask | None = None
    _module: Module | None = None
    _repository: Repository | None = None
    _web_mapper: WebMapper | None = None
    _game_mapper: GameMapper | None = None
    _service: Service | None = None

    @classmethod
    def repo(cls):
        if cls._repository is None:
            cls._repository = Repository(cls.game_mapper())
        return cls._repository

    @classmethod
    def module(cls):
        if cls._module is None:
            cls._module = Module(
                app=cls.app(),
                route=Route(
                    cls.repo(),
                    cls.web_mapper(),
                    cls.service()
                )
            )
        return cls._module
    
    @classmethod
    def app(cls):
        if cls._app is None:
            cls._app = Flask(__name__)
        return cls._app
    
    @classmethod
    def web_mapper(cls):
        if cls._web_mapper is None:
            cls._web_mapper = WebMapper()
        return cls._web_mapper

    @classmethod
    def game_mapper(cls):
        if cls._game_mapper is None:
            cls._game_mapper = GameMapper()
        return cls._game_mapper

    @classmethod
    def service(cls):
        if cls._service is None:
            cls._service = Service()
        return cls._service

    @classmethod
    def run(cls):
        cls.module().register()
        cls.app().run()