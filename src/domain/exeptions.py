
class GameError:
    class NotFound(Exception):
        def __init__(self):
            super().__init__('Game not found.')
        
    class NotYourTurn(Exception):
        def __init__(self):
            super().__init__('Not your turn.')

    class NotInProgress(Exception):
        def __init__(self):
            super().__init__('Game not in progress.')

    class InvalidMove(Exception):
        def __init__(self, message=' '):
            super().__init__('Invalid move. ' + message)

    class Finished(Exception):
        def __init__(self):
            super().__init__('Game is finished.')