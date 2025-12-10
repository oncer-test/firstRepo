#!/usr/bin/env python3
"""
Claude ASCII Art Renderer.

Safely displays predefined Claude ASCII art.
"""

import sys
from typing import TextIO, Optional

def validate_ascii_art(art: Optional[str], max_width: int = 40, max_height: int = 6) -> bool:
    """
    Validate ASCII art for safety and project constraints.

    Args:
        art (Optional[str]): ASCII art to validate
        max_width (int): Maximum allowed width of art
        max_height (int): Maximum allowed height of art

    Returns:
        bool: True if art passes safety checks, False otherwise
    """
    # Comprehensive safety checks
    if art is None:
        return False

    lines = art.splitlines()
    return (
        isinstance(art, str) and
        len(art) > 0 and
        len(art) <= 1024 and  # Reasonable size limit
        len(lines) <= max_height and  # Height constraint
        all(len(line) <= max_width for line in lines) and  # Width constraint
        all(ord(char) < 128 for char in art)  # ASCII only
    )

def render_claude_art(
    art: str,
    file: Optional[TextIO] = None
) -> None:
    """
    Safely render Claude ASCII art.

    Args:
        art (str): ASCII art to render
        file (Optional[TextIO]): Output stream, defaults to sys.stdout

    Raises:
        ValueError: If art fails validation
    """
    if not validate_ascii_art(art):
        raise ValueError("Invalid ASCII art")

    print(art, file=file or sys.stdout)

# Claude ASCII art constant
CLAUDE_ASCII_ART = r''' ____   _     _   _   _  ____
/ ___| | |   | | | | | |/ ___|
| |    | |   | | | | | | |
| |    | |   | | | | | | |
| |___ | |___| | | |_| | |___
 \____||______/  \___/ \____|
'''

def main() -> None:
    """Entry point for rendering Claude ASCII art."""
    render_claude_art(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    main()