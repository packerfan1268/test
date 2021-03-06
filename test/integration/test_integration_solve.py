import unittest

import util
from solve import load_board
from solve import parallel_solve
from solve import serial_solve

three_board = load_board(util.fixture_path('3-colors.png'))
four_board = load_board(util.fixture_path('4-colors.png'))
five_board = load_board(util.fixture_path('5-colors.png'))
six_board = load_board(util.fixture_path('6-colors.png'))
unsolvable_board = load_board(util.fixture_path('unsolvable.png'))


class TestIntegrationSerialSolve(unittest.TestCase):
    def test_serial_solve_three_colors(self):
        self.assert_valid_serial_solve(three_board)

    def test_serial_unsolvable(self):
        self.assert_invalid_serial_solve(unsolvable_board)

    def assert_valid_serial_solve(self, board):
        solution = serial_solve(board)
        self.assertFalse(solution.is_empty())
        self.assertTrue(util.is_solution_valid(board, solution.get_steps()))

    def assert_invalid_serial_solve(self, board):
        solution = serial_solve(board)
        self.assertTrue(solution.is_empty())


class TestIntegrationParallelSolve(unittest.TestCase):
    def test_parallel_solve_three_colors(self):
        self.assert_valid_parallel_solve(three_board)

    def test_parallel_solve_four_colors(self):
        self.assert_valid_parallel_solve(four_board)

    def test_parallel_solve_five_colors(self):
        self.assert_valid_parallel_solve(five_board)

    def test_parallel_solve_six_colors(self):
        self.assert_valid_parallel_solve(six_board)

    def test_parallel_unsolvable(self):
        self.assert_invalid_parallel_solve(unsolvable_board)

    def assert_valid_parallel_solve(self, board):
        solution = parallel_solve(board)
        self.assertFalse(solution.is_empty())
        self.assertTrue(util.is_solution_valid(board, solution.get_steps()))

    def assert_invalid_parallel_solve(self, board):
        solution = parallel_solve(board)
        self.assertTrue(solution.is_empty())
