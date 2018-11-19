
class Kalah(object):
    def __init__(self, holes, seeds):
        self.current_player = 0
        self.game_over = False
        self.board = [seeds] * holes * 2
        self.bank = [0, 0]
        self.holes = holes

    def valid_hole(self, hole):
        if hole not in range(self.holes):
            raise IndexError("invalid index number :(")

        if self.board[hole + self.current_player*self.holes] == 0:
            raise ValueError("cannot play this move no seeds")

    def is_game_over(self):
        if self.game_over:
            if self.bank[0] == self.bank[1]:
                return "tie"
            return "Player 1 wins" if self.bank[1] > self.bank[0] else "Player 2 wins"
        return False

    def play(self, hole):
        self.valid_hole(hole)
        player = self.current_player
        seeds = self.board[hole + player*self.holes]

        self.board[hole + player * self.holes] = 0
        index = hole + player * self.holes + 1
        while seeds:
            if not player and index == self.holes:
                self.bank[0] += 1
                seeds -= 1
                if not seeds:
                    continue
            if player and index == self.holes*2:
                self.bank[1] += 1
                seeds -= 1
                if not seeds:
                    continue
                index = (index + 1) % (self.holes * 2 + 1)

            self.board[index] += 1
            index = (index+1) % (self.holes*2+1)
            seeds -= 1
        if not self.is_game_over():
            if index == self.holes + player * self.holes:
                return f'Player {self.current_player+1} plays next'
            else:
                self.current_player = not self.current_player
                return f'Player {self.current_player+1} plays next'

    def status(self):
        return tuple(self.board[0: self.holes] + [self.bank[0]] + \
                     self.board[self.holes: (self.holes * 2) + 1] + [self.bank[1]])

    def done(self):
        return self.game_over

    def score(self):
        return tuple(self.bank)
