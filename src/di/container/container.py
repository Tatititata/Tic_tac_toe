from datasource import *
from domain import *
from web import *



class Container:
    def __init__(self):
        self._module = Module(Repository(GameMapper()), WebMapper(), Service())

    def run(self):
        self._module.run()