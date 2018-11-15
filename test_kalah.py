import unittest
from kalah import Kalah


class KalahTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Kalah(6, 4)

    def test_init_status(self):
        self.assertEqual(self.game.status(), (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0))

    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()

