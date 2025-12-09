"""
Tic-Tac-Toe Player Implementation

This module provides the Player class for managing player attributes
and move strategies.
"""

from typing import Optional, Tuple
from enum import Enum, auto
import random


class PlayerType(Enum):
    """
    Represents different types of players in the game.

    Allows for human and computer (AI) players.
    """
    HUMAN = auto()
    AI = auto()


class Player:
    """
    Represents a Tic-Tac-Toe player.

    Manages player metadata, symbol, and move generation strategy.

    Attributes:
        name (str): Player's name
        symbol (str): Player's game symbol (X or O)
        player_type (PlayerType): Type of player (human or AI)
    """

    def __init__(
        self,
        name: str,
        symbol: str,
        player_type: PlayerType = PlayerType.HUMAN
    ):
        """
        Initialize a player with given attributes.

        Args:
            name (str): Player's name
            symbol (str): Player's game symbol (X or O)
            player_type (PlayerType, optional): Player type. Defaults to HUMAN.

        Raises:
            ValueError: If symbol is not 'X' or 'O'
        """
        if symbol not in ['X', 'O']:
            raise ValueError("Symbol must be 'X' or 'O'")

        self.name = name
        self.symbol = symbol
        self.player_type = player_type

    def get_move(self, board) -> Tuple[int, int]:
        """
        Generate a move based on player type.

        For human players, this method would typically be overridden
        to get input. For AI, it provides a simple random move strategy.

        Args:
            board: Current game board state

        Returns:
            Tuple[int, int]: Row and column of selected move
        """
        if self.player_type == PlayerType.AI:
            return self._get_ai_move(board)

        raise NotImplementedError("Human player move selection not implemented")

    def _get_ai_move(self, board) -> Tuple[int, int]:
        """
        Generate a random valid move for AI player.

        Finds all empty cells and selects one randomly.

        Args:
            board: Current game board state

        Returns:
            Tuple[int, int]: Row and column of selected move

        Raises:
            ValueError: If no valid moves are available
        """
        # Find all empty cells
        empty_cells = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if board.get_grid()[row][col] == board.CellState.EMPTY
        ]

        if not empty_cells:
            raise ValueError("No valid moves available")

        # Return a random empty cell
        return random.choice(empty_cells)