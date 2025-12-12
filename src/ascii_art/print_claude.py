"""Print Claude's ASCII art to console or file.

Module provides functionality to render Claude's ASCII art with validation.
"""
from typing import Optional, TextIO
from sys import stdout

from .claude import CLAUDE_ASCII_ART, render_claude_art, validate_ascii_art


def print_claude_art(
    art: str = CLAUDE_ASCII_ART,
    file: Optional[TextIO] = None
) -> None:
    """Print Claude ASCII art with safety validation.

    Args:
        art (str, optional): ASCII art to print. Defaults to predefined art.
        file (Optional[TextIO], optional): Output stream. Defaults to stdout.

    Raises:
        ValueError: If art fails validation checks.
    """
    if validate_ascii_art(art):
        render_claude_art(art, file or stdout)


def main() -> None:
    """Entry point for command-line execution."""
    print_claude_art()


if __name__ == '__main__':
    main()