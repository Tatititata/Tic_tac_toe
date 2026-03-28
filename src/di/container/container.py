from datasource import Repository, Mapper, Database, Schema
from domain import Service
from web import WebMapper, Module, Route
from flask import Flask






class Container:
    _app: Flask | None = None
    _module: Module | None = None
    _repo:Repository | None = None
    _web_mapper: WebMapper | None = None
    _mapper: Mapper | None = None
    _service: Service | None = None

    @classmethod
    def repo(cls):
        if cls._repo is None:
            mapper = cls.mapper()
            engine = Database().engine()
            cls._repo = Repository(engine, mapper)
        return cls._repo

    @classmethod
    def module(cls):
        if cls._module is None:
            app = cls.app()
            route = Route(cls.web_mapper(), cls.service())
            cls._module = Module(app, route)
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
    def mapper(cls):
        if cls._mapper is None:
            cls._mapper = Mapper()
        return cls._mapper

    @classmethod
    def service(cls):
        if cls._service is None:
            cls._service = Service(cls.repo())
        return cls._service

    @classmethod
    def run(cls):
        cls.module().register()
        cls.app().run()