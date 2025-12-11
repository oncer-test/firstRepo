#!/usr/bin/env python3
"""
Claude ASCII Art Renderer.

Safely displays predefined Claude ASCII art.
"""

import sys
from typing import TextIO, Optional

def validate_ascii_art(art: str) -> bool:
    """
    Validate ASCII art against strict design constraints.

    Validates:
    - Non-None input
    - String type
    - Non-empty string
    - Maximum length of 1024 characters
    - Strictly ASCII characters
    - Maximum line width of 40 characters
    - Maximum height of 6 lines

    Args:
        art (str): ASCII art to validate

    Returns:
        bool: True if art passes all validation checks, False otherwise
    """
    if art is None or not isinstance(art, str) or len(art) == 0:
        return False

    lines = art.splitlines()
    return (
        len(art) <= 1024 and  # Reasonable size limit
        all(ord(char) < 128 for char in art) and  # ASCII only
        len(lines) <= 6 and  # Maximum height
        all(len(line) <= 40 for line in lines)  # Maximum line width
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
CLAUDE_ASCII_ART = r''' _____  _     ____   _    _   ____
/  __ \| |   / __ \ | |  | | / __ \
| |    | |  | |  | || |  | || |  | |
| |    | |  | |  | || |  | || |  | |
| |____| |__| |__| || |__| || |__| |
 \____/\_____\____/ \____/  \____/ |
'''

def main() -> None:
    """Entry point for rendering Claude ASCII art."""
    render_claude_art(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    main()