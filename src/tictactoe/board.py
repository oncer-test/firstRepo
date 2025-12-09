"""
Tic-Tac-Toe Board Implementation

This module provides the Board class for managing the game board state,
move validation, and win condition detection.
"""

from typing import Optional, List
from enum import Enum, auto


class CellState(Enum):
    """Represents the state of a cell on the Tic-Tac-Toe board."""
    EMPTY = auto()
    X = auto()
    O = auto()


class Board:
    """
    Manages the Tic-Tac-Toe game board state.

    Provides methods for making moves, checking win conditions,
    and managing board state.

    Attributes:
        _grid (List[List[CellState]]): Internal 3x3 grid representation
    """

    def __init__(self):
        """
        Initialize an empty 3x3 Tic-Tac-Toe board.

        The board is represented as a 3x3 grid of CellState,
        initially set to EMPTY.
        """
        self._grid: List[List[CellState]] = [
            [CellState.EMPTY for _ in range(3)]
            for _ in range(3)
        ]

    def make_move(self, row: int, col: int, player: CellState) -> bool:
        """
        Place a player's mark on the board.

        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
            player (CellState): Player's mark (X or O)

        Returns:
            bool: True if move is valid and successful, False otherwise

        Raises:
            ValueError: If row or column indices are out of bounds
        """
        # Validate input coordinates
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Row and column must be between 0 and 2")

        # Check if cell is empty before making move
        if self._grid[row][col] != CellState.EMPTY:
            return False

        # Place player's mark
        self._grid[row][col] = player
        return True

    def check_winner(self) -> Optional[CellState]:
        """
        Check if there's a winner on the board.

        Checks all possible winning combinations:
        - Horizontal rows
        - Vertical columns
        - Two diagonals

        Returns:
            Optional[CellState]: Winning player (X or O) or None if no winner
        """
        # Check rows
        for row in self._grid:
            if row[0] != CellState.EMPTY and len(set(row)) == 1:
                return row[0]

        # Check columns
        for col in range(3):
            column = [self._grid[row][col] for row in range(3)]
            if column[0] != CellState.EMPTY and len(set(column)) == 1:
                return column[0]

        # Check diagonals
        diag1 = [self._grid[i][i] for i in range(3)]
        diag2 = [self._grid[i][2-i] for i in range(3)]

        if diag1[0] != CellState.EMPTY and len(set(diag1)) == 1:
            return diag1[0]
        if diag2[0] != CellState.EMPTY and len(set(diag2)) == 1:
            return diag2[0]

        return None

    def is_board_full(self) -> bool:
        """
        Check if the board is in a draw state.

        Returns:
            bool: True if no empty cells remain, False otherwise
        """
        return all(
            cell != CellState.EMPTY
            for row in self._grid
            for cell in row
        )

    def reset(self) -> None:
        """
        Reset the board to its initial empty state.

        Clears all cells, returning the board to a fresh state.
        """
        self._grid = [
            [CellState.EMPTY for _ in range(3)]
            for _ in range(3)
        ]

    def get_grid(self) -> List[List[CellState]]:
        """
        Retrieve a copy of the current board grid.

        Returns:
            List[List[CellState]]: Current board state
        """
        return [row.copy() for row in self._grid]