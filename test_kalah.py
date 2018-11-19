import unittest
from kalah import Kalah


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalah(6, 4)

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

    def test_Two_simple_moves(self):
        self.assertEqual(self.game.play(0), "Player 2 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0))
        self.assertEqual(self.game.play(0), "Player 1 plays next")
        self.assertEqual(self.game.status(), (0, 5, 5, 5, 5, 4, 0, 0, 5, 5, 5, 5, 4, 0))

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()

