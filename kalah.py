
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
                return "Tie"
            return "Player 1 Wins" if self.bank[0] > self.bank[1] else "Player 2 Wins"
        return False

    def play(self, hole):
        self.valid_hole(hole)
        player = self.current_player
        seeds = self.board[hole + player*self.holes]
        self.board[hole + player * self.holes] = 0
        index = hole + player * self.holes

        while seeds:
            ex = False
            index = (index + 1) % (self.holes * 2)
            if not player and index == self.holes:
                self.bank[0] += 1
                seeds -= 1
                ex = True
                if not seeds:
                    continue

            if player and index == 0:
                self.bank[1] += 1
                seeds -= 1
                if not seeds:
                    continue

            self.board[index] += 1
            if ex and seeds == 1:
                index = (index + 1) % (self.holes * 2)
            seeds -= 1

        opposite_index = self.holes*2-1-index
        if self.board[index] == 1 and self.board[opposite_index] > 0:
            self.bank[player] += self.board[opposite_index]+1
            self.board[index] = 0
            self.board[opposite_index] = 0

        if player and sum(self.board[:self.holes]) == 0:
            self.bank[1] += sum(self.board[self.holes:])
            self.game_over = True

        elif not player and sum(self.board[self.holes:]) == 0:
            self.bank[0] += sum(self.board[:self.holes])
            self.game_over = True
        if self.game_over:
            return self.is_game_over()
        else:
            if (not (index == self.holes and not player)) and (not (index == 0 and player)):
                self.current_player = not self.current_player
            return f'Player {self.current_player+1} plays next'

    def status(self):
        return tuple(self.board[0: self.holes] + [self.bank[0]] + \
                     self.board[self.holes: (self.holes * 2) + 1] + [self.bank[1]])

    def done(self):
        return self.game_over

    def score(self):
        return tuple(self.bank)

    def set_board(self, l_board):
        self.board = l_board

    def set_bank(self, l_bank):
        self.bank = l_bank

