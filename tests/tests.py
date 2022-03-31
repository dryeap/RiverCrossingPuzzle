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

    def test_gameWin(self):
        self.assertTrue(_.isWin(_.State([], [1, 1, 1, 0, 0, 0])))

    def test_gameplayWin(self):
        state = _.State()
        state.move(1, 1)
        state.move(1)
        state.move(1, 1)
        state.move(1)
        state.move(0, 0)
        state.move(0, 1)
        state.move(0, 0)
        state.move(1)
        state.move(1, 1)
        state.move(1)
        state.move(1, 1)
        self.assertTrue(_.isWin(state))


if __name__ == "__main__":
    unittest.main()

# TODO : more tests
