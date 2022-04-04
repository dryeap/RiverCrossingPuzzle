import unittest
from copy import deepcopy

import main.main as _


class MyTestCase(unittest.TestCase):
    def test_initGameOver(self):
        state = _.State([1, 1, 0])
        with self.subTest():
            self.assertTrue(_.isGameOver(state))
        state = _.State([], [1, 1, 0])
        with self.subTest():
            self.assertTrue(_.isGameOver(state))

    def test_initGameNotOver(self):
        state = _.State([1, 1, 0, 0], [0, 1])
        with self.subTest():
            self.assertFalse(_.isGameOver(state))

        state = _.State([1, 0], [1, 1, 0, 0])
        with self.subTest():
            self.assertFalse(_.isGameOver(state))

    def test_move(self):
        state = _.State()
        state.move(1, 1)
        with self.subTest():
            self.assertTrue(state.right == [1, 1] and state.left == [0, 0, 0, 1])

        state.move(1, 1)
        with self.subTest():
            self.assertTrue(state.right == [] and state.left == [0, 0, 0, 1, 1, 1])

        with self.subTest():
            self.assertFalse(state.move(0, 0))  # move into game over

    def test_incompatibleMove(self):
        state = _.State()

        with self.subTest():
            self.assertFalse(state.move())  # empty move

        state.move(1, 1)

        with self.subTest():
            self.assertFalse(state.move(0))  # incompatible move of 1 person

        with self.subTest():
            self.assertFalse(state.move(0, 0))  # incompatible move of 2 same people

        with self.subTest():
            self.assertFalse(state.move(0, 1))  # incompatible move of 2 diff people

    def test_row(self):
        state = _.State()
        state = _.row(state, (1, 1))

        with self.subTest():
            self.assertTrue(state.right == [1, 1] and state.left == [0, 0, 0, 1])

        state = _.row(state, (1, 1))
        with self.subTest():
            self.assertTrue(state.right == [] and state.left == [0, 0, 0, 1, 1, 1])

        # main.row() doesnt change state if move results in game over
        deadState = _.row(deepcopy(state), (0, 0))

        with self.subTest():
            self.assertEqual(state.showStateSimple(), deadState.showStateSimple())  # move into game over

    def test_gameWin(self):
        self.assertTrue(_.isWin(_.State([], [1, 1, 1, 0, 0, 0])))

    def test_printState(self):
        state = _.State()

        with self.subTest():
            self.assertEqual(str(state.showStateSimple()), "([0, 0, 0, 1, 1, 1], '_ ', [])")

        with self.subTest():
            self.assertEqual(str(state.showStatePretty()), "🕋, 🕋, 🕋, 👿, 👿, 👿 🚤 ___ ")

    def test_winningMoves(self):
        state = _.State()

        move_sequence = [
            [1, 1],
            [1],
            [1, 1],
            [1],
            [0, 0],
            [0, 1],
            [0, 0],
            [1],
            [1, 1],
            [1],
            [1, 1],
        ]

        [state.move(*m) for m in move_sequence]

        self.assertTrue(_.isWin(state))

    def test_notWin(self):
        state = _.State()
        self.assertFalse(_.isWin(state))

    def test_manualPlayGameOver(self):
        state = _.State([0, 1, 1])
        self.assertFalse(_.manualPlay(state))

    def test_manualPlayWin(self):
        state = _.State([], [0, 0, 0, 1, 1, 1])
        self.assertTrue(_.manualPlay(state))

    def test_solve(self):
        _.solve(_.State(), "dfs")
        # check size of stack, seen states and counter
        with self.subTest():
            self.assertTupleEqual((len(_.q), len(_.seen), _.ctr), (9, 25, 16))

        # reset vars
        _.q, _.seen, _.ctr = [], [], 0

        _.solve(_.State(), "bfs")
        # check size of queue, seen states and counter
        with self.subTest():
            self.assertTupleEqual((len(_.q), len(_.seen), _.ctr), (2, 30, 28))


# TODO : test manualPlay() with mock input
# TODO : test solve (if it always wins)

if __name__ == "__main__":
    unittest.main()
