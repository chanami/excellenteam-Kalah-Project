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

    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()

