import unittest
import main.main as _


class MyTestCase(unittest.TestCase):
    def test_gameOverLeft(self):
        state = _.State([1, 1, 0])
        self.assertTrue(_.isGameOver(state))

    def test_gameOverRight(self):
        state = _.State([], [1, 1, 0])
        self.assertTrue(_.isGameOver(state))

    def test_gameNotOver1(self):
        state = _.State([1, 1, 0, 0], [0, 1])
        self.assertFalse(_.isGameOver(state))

    def test_gameNotOver2(self):
        state = _.State([1, 0], [1, 1, 0, 0])
        self.assertFalse(_.isGameOver(state))


if __name__ == '__main__':
    unittest.main()
