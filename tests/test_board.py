"""
Unit tests for the Tic-Tac-Toe Board class.

Tests cover board initialization, move validation,
win condition detection, and board state management.
"""

import pytest
from src.tictactoe.board import Board, CellState


class TestBoard:
    """Test suite for the Board class."""

    def setup_method(self):
        """
        Create a fresh Board instance before each test.
        Ensures test isolation and clean state.
        """
        self.board = Board()

    def test_initial_board_empty(self):
        """
        Verify that a new board is completely empty.
        """
        grid = self.board.get_grid()
        assert all(
            cell == CellState.EMPTY
            for row in grid
            for cell in row
        )

    def test_valid_move(self):
        """
        Ensure valid moves are correctly placed on the board.
        """
        # Test placing X at various positions
        for row in range(3):
            for col in range(3):
                # Reset board before each test
                self.board.reset()
                assert self.board.make_move(row, col, CellState.X)
                grid = self.board.get_grid()
                assert grid[row][col] == CellState.X

    def test_invalid_move_occupied(self):
        """
        Verify that moves on already occupied cells are rejected.
        """
        self.board.make_move(1, 1, CellState.X)
        assert not self.board.make_move(1, 1, CellState.O)

    def test_move_out_of_bounds(self):
        """
        Check that out-of-bounds moves raise a ValueError.
        """
        with pytest.raises(ValueError):
            self.board.make_move(3, 3, CellState.X)
        with pytest.raises(ValueError):
            self.board.make_move(-1, -1, CellState.O)

    def test_horizontal_win(self):
        """
        Test horizontal win detection.
        """
        # Test each row for winning condition
        for row_idx in range(3):
            self.board.reset()
            for col in range(3):
                self.board.make_move(row_idx, col, CellState.X)

            assert self.board.check_winner() == CellState.X

    def test_vertical_win(self):
        """
        Test vertical win detection.
        """
        # Test each column for winning condition
        for col_idx in range(3):
            self.board.reset()
            for row in range(3):
                self.board.make_move(row, col_idx, CellState.O)

            assert self.board.check_winner() == CellState.O

    def test_diagonal_wins(self):
        """
        Test both diagonal win conditions.
        """
        # Test main diagonal (top-left to bottom-right)
        for player in [CellState.X, CellState.O]:
            self.board.reset()
            for i in range(3):
                self.board.make_move(i, i, player)
            assert self.board.check_winner() == player

            # Test anti-diagonal (top-right to bottom-left)
            self.board.reset()
            for i in range(3):
                self.board.make_move(i, 2-i, player)
            assert self.board.check_winner() == player

    def test_board_full(self):
        """
        Verify board full detection without a winner.
        """
        # Alternate X and O to fill the board
        players = [CellState.X, CellState.O]
        for row in range(3):
            for col in range(3):
                self.board.make_move(row, col, players[(row + col) % 2])

        assert self.board.is_board_full()
        assert self.board.check_winner() is None

    def test_board_reset(self):
        """
        Ensure board reset returns all cells to EMPTY.
        """
        # Fill board first
        for row in range(3):
            for col in range(3):
                self.board.make_move(row, col, CellState.X)

        self.board.reset()
        grid = self.board.get_grid()
        assert all(
            cell == CellState.EMPTY
            for row in grid
            for cell in row
        )