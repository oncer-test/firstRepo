"""
Unit tests for the Tic-Tac-Toe Player class.

Tests cover player initialization, move generation,
and player type handling.
"""

import pytest
import random
from src.tictactoe.board import Board, CellState
from src.tictactoe.player import Player, PlayerType


class TestPlayer:
    """Test suite for the Player class."""

    def setup_method(self):
        """
        Setup method to create a fresh Board and Player instances.
        Ensures test isolation.
        """
        self.board = Board()
        # Seed random for reproducible AI move tests
        random.seed(42)

    def test_player_creation(self):
        """
        Test player initialization with valid parameters.
        """
        player_x = Player("Alice", "X")
        assert player_x.name == "Alice"
        assert player_x.symbol == "X"
        assert player_x.player_type == PlayerType.HUMAN

        player_o = Player("Bob", "O", PlayerType.AI)
        assert player_o.name == "Bob"
        assert player_o.symbol == "O"
        assert player_o.player_type == PlayerType.AI

    def test_invalid_player_symbol(self):
        """
        Verify that invalid symbols raise a ValueError.
        """
        with pytest.raises(ValueError):
            Player("Charlie", "A")
        with pytest.raises(ValueError):
            Player("Dave", "")

    def test_ai_move_generation(self):
        """
        Test AI move generation on an empty board.
        """
        # Setup an AI player
        ai_player = Player("AI", "X", PlayerType.AI)

        # Test multiple AI moves on an empty board
        for _ in range(5):  # Multiple random move tests
            move = ai_player.get_move(self.board)
            assert isinstance(move, tuple)
            assert len(move) == 2
            row, col = move
            assert 0 <= row < 3
            assert 0 <= col < 3
            # Verify the cell is empty
            assert self.board.get_grid()[row][col] == CellState.EMPTY

    def test_ai_move_on_partially_filled_board(self):
        """
        Test AI move generation on a partially filled board.
        """
        # Fill some cells
        self.board.make_move(0, 0, CellState.X)
        self.board.make_move(1, 1, CellState.O)

        ai_player = Player("AI", "X", PlayerType.AI)
        move = ai_player.get_move(self.board)
        row, col = move
        # Verify move is on an empty cell
        assert self.board.get_grid()[row][col] == CellState.EMPTY

    def test_human_player_move_not_implemented(self):
        """
        Verify that get_move for human players raises NotImplementedError.
        """
        human_player = Player("Human", "O")
        with pytest.raises(NotImplementedError):
            human_player.get_move(self.board)

    def test_no_moves_available(self):
        """
        Test AI move generation when board is full.
        """
        # Fill the entire board
        for row in range(3):
            for col in range(3):
                self.board.make_move(row, col, CellState.X)

        ai_player = Player("AI", "O", PlayerType.AI)
        with pytest.raises(ValueError):
            ai_player.get_move(self.board)