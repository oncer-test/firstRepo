"""
Claude ASCII Art Rendering and Validation Module

Ensures precise rendering of Claude's ASCII art with robust validation.
"""

import re
from typing import List, Optional


class AsciiArtValidationError(ValueError):
    """Custom exception for ASCII art validation failures."""
    pass


def validate_ascii_art(art_lines: List[str]) -> None:
    """
    Validate ASCII art against specified constraints.

    Args:
        art_lines (List[str]): Lines of ASCII art to validate

    Raises:
        AsciiArtValidationError: If art does not meet validation constraints
    """
    # Check total number of lines
    if len(art_lines) != 6:
        raise AsciiArtValidationError(f"Must have exactly 6 lines, got {len(art_lines)}")

    # Check each line's width
    for i, line in enumerate(art_lines):
        if len(line) > 40:
            raise AsciiArtValidationError(f"Line {i+1} exceeds 40 characters (got {len(line)})")

        # Ensure ASCII-only characters
        if not all(ord(char) < 128 for char in line):
            raise AsciiArtValidationError(f"Line {i+1} contains non-ASCII characters")


def render_claude_ascii_art() -> str:
    """
    Render the canonical Claude ASCII art.

    Returns:
        str: Multiline ASCII art representation of Claude
    """
    claude_ascii_art = [
        " _____  _    _   _      _   _  ____",
        "/ ____|| |  | | | |    | | | |/ __ \\",
        "| |    | |  | | | |    | | | | |  | |",
        "| |    | |  | | | |    | | | | |  | |",
        "| |____| |__| | | |____| |_| | |__| |",
        " \\_____|\____/  |______\\___/ \\____/"
    ]

    # Validate the art before rendering
    validate_ascii_art(claude_ascii_art)

    return "\n".join(claude_ascii_art)


def main():
    """
    Print the Claude ASCII art with validation.
    """
    try:
        print(render_claude_ascii_art())
    except AsciiArtValidationError as e:
        print(f"ASCII Art Validation Error: {e}")
        raise


if __name__ == "__main__":
    main()