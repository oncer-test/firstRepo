#!/usr/bin/env python3
"""
Claude ASCII Art Renderer.

Safely displays predefined Claude ASCII art.
"""

import sys
from typing import TextIO, Optional, List

def is_ascii_only(text: str) -> bool:
    """Check if a string contains only ASCII characters."""
    return all(ord(char) < 128 for char in text)

def validate_line_width(lines: List[str], max_width: int = 40) -> bool:
    """Validate line width against max constraint."""
    return all(len(line) <= max_width for line in lines)

def validate_ascii_art(
    art: str,
    max_width: int = 40,
    max_height: int = 6
) -> bool:
    """
    Validate ASCII art against strict safety constraints.

    Args:
        art (str): ASCII art to validate
        max_width (int): Maximum line width
        max_height (int): Maximum number of lines

    Returns:
        bool: True if art passes all safety checks
    """
    if not art or not isinstance(art, str):
        return False

    lines = art.strip().splitlines()

    return (
        bool(lines) and
        len(lines) <= max_height and
        all(is_ascii_only(line) for line in lines) and
        validate_line_width(lines, max_width)
    )

def render_claude_art(
    art: str,
    file: Optional[TextIO] = None
) -> None:
    """
    Safely render Claude ASCII art to output stream.

    Args:
        art (str): ASCII art to render
        file (TextIO, optional): Output destination, defaults to sys.stdout

    Raises:
        ValueError: If art fails validation
    """
    if not validate_ascii_art(art):
        raise ValueError("Invalid ASCII art")

    print(art.strip(), file=file or sys.stdout)

# Claude ASCII art constant
CLAUDE_ASCII_ART = r"""    _____  _    _  _____
   / ____|/ \  | |/ ____|
  | |    / _ \ | | |
  | |   / ___ \| | |
  |____/_/   \_\_|\_____|"""

def main() -> None:
    """Entry point for rendering Claude ASCII art."""
    render_claude_art(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    main()