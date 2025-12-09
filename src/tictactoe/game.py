"""
Tic-Tac-Toe Game Implementation

This module provides the core game logic for a Tic-Tac-Toe game,
managing game flow, player turns, and game state.
"""

from enum import Enum, auto
from typing import Optional

from .board import Board, CellState
from .player import Player, PlayerType


class GameState(Enum):
    """
    Represents the current state of the Tic-Tac-Toe game.

    Tracks ongoing game, win conditions, and draw scenarios.
    """
    ONGOING = auto()
    X_WINS = auto()
    O_WINS = auto()
    DRAW = auto()


class TicTacToeGame:
    """
    Manages the complete Tic-Tac-Toe game flow.

    Coordinates board state, player turns, and game progression.

    Attributes:
        board (Board): Game board instance
        player_x (Player): Player using X symbol
        player_o (Player): Player using O symbol
    """

    def __init__(
        self,
        player_x: Optional[Player] = None,
        player_o: Optional[Player] = None
    ):
        """
        Initialize the game with optional custom players.

        Args:
            player_x (Optional[Player]): X player, defaults to human player
            player_o (Optional[Player]): O player, defaults to human player
        """
        self.board = Board()
        self.player_x = player_x or Player("Player X", "X")
        self.player_o = player_o or Player("Player O", "O")
        self.current_player = self.player_x

    def switch_player(self) -> None:
        """
        Switch the current active player.

        Alternates between X and O players.
        """
        self.current_player = (
            self.player_o if self.current_player == self.player_x
            else self.player_x
        )

    def play_turn(self) -> GameState:
        """
        Execute a single game turn.

        Determines current player, gets their move, updates board,
        and checks game state.

        Returns:
            GameState: Updated game state after turn
        """
        # Determine player symbol based on current player
        current_symbol = (
            CellState.X if self.current_player == self.player_x
            else CellState.O
        )

        try:
            # Get player's move
            row, col = self.current_player.get_move(self.board)

            # Attempt to make move
            if not self.board.make_move(row, col, current_symbol):
                # Invalid move, game continues
                return self.get_game_state()

        except (ValueError, NotImplementedError):
            # Move generation failed, game continues
            return self.get_game_state()

        # Switch to next player after successful move
        self.switch_player()

        # Return updated game state
        return self.get_game_state()

    def get_game_state(self) -> GameState:
        """
        Determine the current game state.

        Checks for win conditions or draw scenario.

        Returns:
            GameState: Current game state
        """
        winner = self.board.check_winner()

        if winner == CellState.X:
            return GameState.X_WINS
        elif winner == CellState.O:
            return GameState.O_WINS
        elif self.board.is_board_full():
            return GameState.DRAW
        else:
            return GameState.ONGOING

    def run(
        self,
        max_turns: int = 9
    ) -> GameState:
        """
        Main game execution method.

        Plays game turns until a conclusion is reached.

        Args:
            max_turns (int, optional): Maximum number of turns. Defaults to 9.

        Returns:
            GameState: Final game result
        """
        current_turn = 0
        game_state = GameState.ONGOING

        while (
            game_state == GameState.ONGOING and
            current_turn < max_turns
        ):
            game_state = self.play_turn()
            current_turn += 1

        return game_state