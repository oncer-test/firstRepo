"""
Unit tests for the Tic-Tac-Toe Game class.

Tests cover game initialization, turn management,
and game state detection.
"""

import pytest
from src.tictactoe.game import TicTacToeGame, GameState
from src.tictactoe.player import Player, PlayerType


class MockAIPlayer(Player):
    """
    Mock AI player for deterministic testing.

    Allows predefined move sequences.
    """
    def __init__(self, name: str, symbol: str, moves):
        """
        Initialize mock AI with predefined moves.

        Args:
            name (str): Player name
            symbol (str): Player symbol
            moves (list): Sequence of predefined moves
        """
        super().__init__(name, symbol, PlayerType.AI)
        self._moves = moves
        self._move_index = 0

    def get_move(self, board):
        """
        Return predefined moves in sequence.

        Args:
            board: Current game board

        Returns:
            tuple: Predefined move
        """
        if self._move_index >= len(self._moves):
            raise ValueError("No more predefined moves")

        move = self._moves[self._move_index]
        self._move_index += 1
        return move


class TestTicTacToeGame:
    """Test suite for TicTacToeGame class."""

    def test_game_initialization(self):
        """
        Verify game initialization with default players.
        """
        game = TicTacToeGame()
        assert game.current_player.symbol == "X"

    def test_player_switching(self):
        """
        Verify player switching mechanism.
        """
        game = TicTacToeGame()
        initial_player = game.current_player
        game.switch_player()
        assert game.current_player != initial_player

    def test_x_wins_scenario(self):
        """
        Test a scenario where X wins the game.
        """
        # Create mock AI players with predetermined winning moves
        x_player = MockAIPlayer("X", "X", [
            (0, 0), (1, 0), (2, 0)  # Vertical win
        ])
        o_player = MockAIPlayer("O", "O", [
            (0, 1), (1, 1)  # Random moves
        ])

        game = TicTacToeGame(x_player, o_player)
        final_state = game.run()

        assert final_state == GameState.X_WINS

    def test_o_wins_scenario(self):
        """
        Test a scenario where O wins the game.
        """
        # Create mock AI players with predetermined winning moves
        x_player = MockAIPlayer("X", "X", [
            (0, 0), (1, 1), (2, 2)  # Random moves
        ])
        o_player = MockAIPlayer("O", "O", [
            (0, 1), (0, 2), (0, 0)  # Horizontal win
        ])

        game = TicTacToeGame(x_player, o_player)
        final_state = game.run()

        assert final_state == GameState.O_WINS

    def test_draw_scenario(self):
        """
        Test a game that results in a draw.
        """
        # Create mock AI players with moves that fill the board without a winner
        x_player = MockAIPlayer("X", "X", [
            (0, 0), (0, 2), (1, 1),
            (2, 0), (2, 2)
        ])
        o_player = MockAIPlayer("O", "O", [
            (0, 1), (1, 0), (1, 2),
            (2, 1), (2, 0)
        ])

        game = TicTacToeGame(x_player, o_player)
        final_state = game.run()

        assert final_state == GameState.DRAW

    def test_max_turns_limit(self):
        """
        Verify game stops after maximum allowed turns.
        """
        # Create mock AI players that would play forever
        x_player = MockAIPlayer("X", "X", [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ])
        o_player = MockAIPlayer("O", "O", [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ])

        game = TicTacToeGame(x_player, o_player)
        final_state = game.run(max_turns=5)

        # Should end in ongoing state if no winner in 5 turns
        assert final_state == GameState.ONGOING