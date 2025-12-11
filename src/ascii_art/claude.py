#!/usr/bin/env python3
"""Claude ASCII Art Renderer.

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

    Raises:
        ValueError: If art fails critical validation
    """
    if not art:
        raise ValueError("ASCII art cannot be empty")

    # Split art into lines
    lines = art.splitlines()

    # Validate line count and width
    if len(lines) > 6:
        raise ValueError(f"ASCII art exceeds max height (6 lines). Current height: {len(lines)}")

    # Check line width
    max_width = max(len(line) for line in lines)
    if max_width > 40:
        raise ValueError(f"ASCII art line exceeds max width (40 chars). Max width: {max_width}")

    # ASCII character check
    try:
        art.encode('ascii')
    except UnicodeEncodeError:
        raise ValueError("ASCII art contains non-ASCII characters")

    return True

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
    validate_ascii_art(art)
    print(art, file=file or sys.stdout)

# Claude ASCII art constant
CLAUDE_ASCII_ART = r''' _____  _    _    ___   _   _  ____
/ ____|| |  | |  / _ \ | | | |/ __ \
| |    | |  | | | | | || | | | |  | |
| |    | |  | | | | | || | | | |  | |
| |____| |__| | | |_| || |_| | |__| |
 \_____|\____/   \___/  \___/ \____/'''

def main() -> None:
    """Entry point for rendering Claude ASCII art."""
    render_claude_art(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    main()