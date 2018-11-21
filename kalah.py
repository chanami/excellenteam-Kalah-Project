import chess

import chess.svg
from IPython.display import SVG

import matplotlib.pyplot as plt
import numpy as np

class Kalah(object):
    def __init__(self, holes, seeds):
        self.current_player = 0
        self.is_game_over = False
        self.board = [seeds] * holes * 2
        self.bank = [0, 0]
        self.holes = holes
        self.seeds=seeds

    def __repr__(self):
        return f"Kalah({self.seeds}, {self.holes}, status={self.status()}, player={self.current_player})"

    def valid_hole(self, hole):
        if hole not in range(self.holes):
            raise IndexError("invalid index number :(")

        if self.board[hole + self.current_player*self.holes] == 0:
            raise ValueError("cannot play this move no seeds")

    def check_if_capture(self,index,opposite_index):
        self.bank[self.current_player] += self.board[opposite_index] + 1
        self.board[index] = 0
        self.board[opposite_index] = 0

    def check_if_game_over(self):
        if self.current_player and sum(self.board[:self.holes]) == 0:
            self.bank[1] += sum(self.board[self.holes:])
            self.is_game_over = True

        elif not self.current_player and sum(self.board[self.holes:]) == 0:
            self.bank[0] += sum(self.board[:self.holes])
            self.is_game_over = True

    def game_over(self):
        if self.bank[0] == self.bank[1]:
            return "Tie"
        return "Player 1 Wins" if self.bank[0] > self.bank[1] else "Player 2 Wins"

    def play(self, hole):
        self.valid_hole(hole)
        player = self.current_player
        bank_exception_flag = False
        seeds = self.board[hole + player*self.holes]
        index = hole + player * self.holes
        self.board[index] = 0

        while seeds:
            bank_exception_flag = False
            index = (index + 1) % (self.holes * 2)
            if not player and index == self.holes:
                self.bank[0] += 1
                seeds -= 1
                bank_exception_flag = True
                if not seeds:
                    continue

            if player and index == 0:
                self.bank[1] += 1
                seeds -= 1
                bank_exception_flag = True
                if not seeds:
                    continue

            self.board[index] += 1
            if bank_exception_flag and seeds == 1:
                index = (index + 1) % (self.holes * 2)
            seeds -= 1

        opposite_index = self.holes*2-1-index
        if self.board[index] == 1 and self.board[opposite_index] > 0:
            self.check_if_capture(index, opposite_index)

        self.check_if_game_over()

        if self.is_game_over:
            return self.game_over()

        elif (not (index == self.holes and not player)) and (not (index == 0 and player and bank_exception_flag)):
            self.current_player = not self.current_player
        return f'Player {self.current_player+1} plays next'

    def status(self):
        return tuple(self.board[0: self.holes] + [self.bank[0]] + \
                     self.board[self.holes: (self.holes * 2) + 1] + [self.bank[1]])

    def done(self):
        return self.is_game_over

    def score(self):
        return tuple(self.bank)

    def set_board(self, l_board):
        self.board = l_board

    def set_bank(self, l_bank):
        self.bank = l_bank

    def board_render(self):
        """Renders the current board to a viewable string"""
        # There are certainly better ways to render this
        board = self.board[:self.holes] + [self.bank[0]] + self.board[self.holes:] + [self.bank[1]]
        result = '    {0: >2} {1: >2} {2: >2} {3: >2} {4: >2} {5: >2}\n'.format(
            board[0], board[1], board[2],
            board[3], board[4], board[5])
        result += ' {0: >2}                   {1: >2} \n'.format(
            board[13], board[6])
        result += '    {0: >2} {1: >2} {2: >2} {3: >2} {4: >2} {5: >2}'.format(
            board[12], board[11], board[10],
            board[9], board[8], board[7])
        return result

    def seeds_format(self,num):
        if num > 4:
            return "." * 4 + "\n" + "." * (num - 4)
        return "." * num

    def svg_render(self):
        board = self.board[:self.holes] + [self.bank[0]] + self.board[self.holes:] + [self.bank[1]]
        nrows, ncols = 2, 8

        image = np.zeros(nrows * ncols)
        image[:self.holes+1:2] = (76)
        image[1:self.holes+1:2] = (4)
        image[self.holes::2] = (4)
        image[self.holes+1::2] = (76)
        image[0] = 18
        image[6] = 76
        image[7] = 18
        image[8] = 18
        image[15] = 18
        image = image.reshape((nrows, ncols))
        col_labels = ['BANK 2', 'A', 'B', 'C', 'D', 'E', 'F', 'BANK 1']
        plt.matshow(image)
        plt.xticks(range(ncols), col_labels)
        print(board)

        for i in range(0, len(board)):
            text = self.seeds_format(board[i])
            if i < 6:
                plt.text(i - 0.3 + 1, 0, text+str(i), fontsize=40)
            elif i == 6:
                plt.text(7, 0.5, text+str(i), fontsize=40)
            elif i == len(board)-1:
                plt.text(0, 0.5, text+str(i), fontsize=40)
            else:
                plt.text(i-6.5, 1, text+str(i), fontsize=40)

        plt.show()


