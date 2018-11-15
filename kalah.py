
class Kalah(object):
    def __init__(self, holes, seeds):
        self.mankala_board = {"player1": [seeds]*holes +[0], "player2": [seeds]*holes +[0]}

    def status(self):
        return tuple(self.mankala_board["player1"])+ tuple(self.mankala_board["player2"])
