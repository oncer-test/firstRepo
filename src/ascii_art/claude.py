#!/usr/bin/env python3
"""
Claude ASCII Art Renderer.

Safely displays predefined Claude ASCII art.
"""

import sys
from typing import TextIO, Optional

def validate_ascii_art(art: str) -> bool:
    """
    Validate ASCII art for safety.

    Args:
        art (str): ASCII art to validate

    Returns:
        bool: True if art passes safety checks, False otherwise
    """
    # Basic safety checks
    return (
        art is not None and
        isinstance(art, str) and
        len(art) > 0 and
        len(art) <= 1024 and  # Reasonable size limit
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
CLAUDE_ASCII_ART = r'''
  _______ _        _        ______ _______
 |__   __| |      | |      |  ____|__   __|
    | |  | |      | |      | |__     | |
    | |  | |      | |      |  __|    | |
    | |  | |____  | |____  | |____   | |
    |_|  |______| |______| |______|  |_|
'''

def main() -> None:
    """Entry point for rendering Claude ASCII art."""
    render_claude_art(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    main()