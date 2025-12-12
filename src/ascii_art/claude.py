#!/usr/bin/env python3
"""
Claude ASCII Art Renderer.

Safely displays predefined Claude ASCII art.
"""

import sys
from typing import TextIO, Optional, Tuple


def validate_ascii_art(art: str) -> Tuple[bool, Optional[str]]:
    """
    Validate ASCII art for safety.

    Args:
        art (str): ASCII art to validate

    Returns:
        Tuple[bool, Optional[str]]: Validation status and optional error message
    """
    # Basic safety checks
    if art is None:
        return False, "Art cannot be None"

    if not isinstance(art, str):
        return False, "Art must be a string"

    if len(art) == 0:
        return False, "Art cannot be empty"

    if len(art) > 1024:
        return False, "Art cannot exceed 1024 characters"

    # ASCII-only check
    if not all(ord(char) < 128 for char in art):
        return False, "Art must contain only ASCII characters"

    # Line width check
    lines = art.splitlines()
    if len(lines) > 6:
        return False, "Art cannot exceed 6 lines"

    if any(len(line) > 40 for line in lines):
        return False, "Each line must be 40 characters or less"

    return True, None


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
    is_valid, error_msg = validate_ascii_art(art)
    if not is_valid:
        raise ValueError(f"Invalid ASCII art: {error_msg}")

    print(art, file=file or sys.stdout)


# Claude ASCII art constant
CLAUDE_ASCII_ART = r''' _____  _    _    ___   _   _  ____
/ ____|| |  | |  / _ \ | | | |/ __ \
| |    | |  | | | | | || | | | |  | |
| |    | |  | | | | | || | | | |  | |
| |____| |__| | | |_| || |_| | |__| |
 \_____|\____/   \___/  \___/ \____/
'''


def main() -> None:
    """Entry point for rendering Claude ASCII art."""
    render_claude_art(CLAUDE_ASCII_ART)


if __name__ == '__main__':
    main()