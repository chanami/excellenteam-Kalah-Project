import unittest
from kalah import Kalah


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalah(6, 4)
        self.game1 = Kalah(6, 6)

    def test_init_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_illegal_hole(self):
        self.assertRaises(IndexError, self.game.play, 8)

    def test_empty_hole(self):
        self.game.board[1] = 0
        self.assertRaises(ValueError, self.game.play, 1)

    def test_game_over(self):
        self.assertEqual(self.game.done(), False)

    def test_get_score(self):
        self.assertEqual(self.game.score(), (0,0))

    def test_simple_move(self):
        self.assertEqual(self.game.play(0),"Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def test_Crossing_move(self):
        self.assertEqual(self.game.play(3), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 4, 0))
        # self.assertEqual(self.game.play(3), "Player 2 plays next")
        # self.assertEqual(self.game.status(), (5, 4, 4, 0, 5, 5, 1, 5, 4, 4, 0, 5, 5, 1))

    def test_Two_simple_moves(self):
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(0), "Player 1 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0))

    def test_Player_2_crosses(self):
        self.assertEqual(self.game.play(5), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 1, 5, 5, 5, 4, 4, 4, 0))
        self.assertEqual(self.game.play(0), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 0, 1, 0, 6, 6, 5, 5, 5, 0))
        self.assertEqual(self.game.play(4), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 0, 1, 2, 1, 7, 6, 5, 5, 5, 0))
        self.assertEqual(self.game.play(1), "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 5, 4, 4, 0, 1, 2, 1, 0, 7, 6, 6, 6, 1))
        self.assertEqual(self.game.play(3), "Player 2 plays next")
        self.assertEqual(self.game.status(), (5, 5, 4, 0, 1, 2, 3, 2, 0, 7, 6, 6, 6, 1))
        self.assertEqual(self.game.play(0), "Player 1 plays next")
        self.assertEqual(self.game.status(), (5, 5, 4, 0, 1, 2, 3, 0, 1, 8, 6, 6, 6, 1))
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 6, 5, 1, 2, 3, 3, 0, 1, 8, 6, 6, 6, 1))
        self.assertEqual(self.game.play(1), "Player 1 plays next")
        self.assertEqual(self.game.status(), (0, 6, 5, 1, 2, 3, 3, 0, 0, 9, 6, 6, 6, 1))

    def test_Crossing_other_bank(self):
        self.game.set_board([0,0,0,0,0,9,1,1,1,1,1,1])
        self.assertEqual(self.game.status(), (0, 0, 0, 0, 0, 9, 0, 1, 1, 1, 1, 1, 1, 0))
        self.assertEqual(self.game.play(5), "Player 2 plays next")
        self.assertEqual(self.game.status(), (1, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 0, 2, 0))

    def test_empty_hole_2(self):
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(0), "Player 1 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0))
        self.assertRaises(ValueError, self.game.play, 0)

    def test_bonus_move_player1(self):
        self.assertEqual(self.game.play(2), "Player 1 plays next")
        self.assertEqual(self.game.status(), (4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0))

    def test_bonus_move_player2(self):
        self.assertEqual(self.game.play(3), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(2), "Player 2 plays next")
        self.assertEqual(self.game.status(), (4, 4, 4, 0, 5, 5, 1, 5, 4, 0, 5, 5, 5, 1))

    def test_capture_player1(self):
        self.game.set_board([2, 0, 0, 0, 0, 9, 1, 3, 1, 1, 1, 1])
        self.assertEqual(self.game.status(), (2, 0, 0, 0, 0, 9, 0, 1, 3, 1, 1, 1, 1, 0))

    def test_capture_player2(self):
        self.game.set_board([2, 0, 0, 0, 0, 9, 1, 3, 1, 1, 0, 9])
        self.assertEqual(self.game.status(), (2, 0, 0, 0, 0, 9, 0, 1, 3, 1, 1, 0, 9, 0))
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 1, 0, 0, 0, 9, 2, 1, 3, 1, 0, 0, 9, 0))
        self.assertEqual(self.game.play(1), "Player 1 plays next")
        self.assertEqual(self.game.status(), (0, 0, 0, 0, 0, 9, 2, 1, 0, 2, 1, 0, 9, 2))

    def test_none_capture(self):
        self.game.set_board([2, 0, 0, 0, 0, 9, 1, 3, 1, 0, 0, 9])
        self.assertEqual(self.game.status(), (2, 0, 0, 0, 0, 9, 0, 1, 3, 1, 0, 0, 9, 0))
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 1, 1, 0, 0, 9, 0, 1, 3, 1, 0, 0, 9, 0))

    def test_game_over_capture2(self):
        self.game.set_board([0, 0, 0, 0, 0, 2, 1, 3, 1, 0, 0, 9])
        self.assertEqual(self.game.status(), (0, 0, 0, 0, 0, 2, 0, 1, 3, 1, 0, 0, 9, 0))
        self.assertEqual(self.game.play(5), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 0, 0, 9, 0))
        self.assertEqual(self.game.play(0), "Player 2 Wins")

    def test_game_over_capture1(self):
        self.game.set_board([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.game.set_bank([20,10])
        self.assertEqual(self.game.status(), (0, 0, 2, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 10))
        self.assertEqual(self.game.play(2), "Player 1 Wins")

    def test_game_over_tie(self):
        self.game.set_board([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.game.set_bank([10, 12])
        self.assertEqual(self.game.status(), (0, 0, 2, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 12))
        self.assertEqual(self.game.play(2), "Tie")

    def test_game_over_bonus(self):
        self.game.set_board([0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0])
        self.game.set_bank([14, 12])
        self.assertEqual(self.game.status(), (0, 0, 0, 0, 2, 0, 14, 0, 0, 0, 0, 0, 0, 12))
        self.assertEqual(self.game.play(4), "Player 1 Wins")





    def test_init_status_6(self):
        self.assertEqual(self.game1.status(), (6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0))

    def test_illegal_hole_6(self):
        self.assertRaises(IndexError, self.game1.play, 8)

    def test_empty_hole_6(self):
        self.game1.board[1] = 0
        self.assertRaises(ValueError, self.game1.play, 1)

    def test_game_over_6(self):
        self.assertEqual(self.game1.done(), False)

    def test_get_score_6(self):
        self.assertEqual(self.game1.score(), (0,0))

    def test_simple_move_(self):
        self.assertEqual(self.game1.play(1), "Player 2 plays next")
        self.assertEqual(self.game1.status(), (6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0))

    def test_Crossing_move_6(self):
        self.assertEqual(self.game1.play(3), "Player 2 plays next")
        self.assertEqual(self.game1.status(), (6, 6, 6, 0, 7, 7, 1, 7, 7, 7, 6, 6, 6, 0))

    def test_Two_simple_moves_6(self):
        self.assertEqual(self.game1.play(1), "Player 2 plays next")
        self.assertEqual(self.game1.status(), (6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0))
        self.assertEqual(self.game1.play(0), "Player 1 plays next")
        self.assertEqual(self.game1.status(), (7, 0, 7, 7, 7, 7, 1, 0, 7, 7, 7, 7, 7, 1))

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()

