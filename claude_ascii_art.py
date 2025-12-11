"""
Claude ASCII Art Rendering Module

Provides safe rendering of Claude's ASCII art representation.
"""

import re
from typing import List, Optional


def validate_ascii_art(art: List[str]) -> Optional[List[str]]:
    """
    Validate ASCII art against design constraints.

    Args:
        art (List[str]): Lines of ASCII art to validate

    Returns:
        Optional[List[str]]: Validated art or None if invalid
    """
    # Validate maximum height
    if len(art) > 6:
        return None

    # Validate each line's width and characters
    for line in art:
        # Check line width
        if len(line) > 40:
            return None

        # Ensure only ASCII characters
        if not re.match(r'^[ -~]*$', line):
            return None

    return art


def render_claude_ascii_art() -> str:
    """
    Render the canonical Claude ASCII art.

    Returns:
        str: Formatted ASCII art representing Claude
    """
    claude_art = [
        "  ____   _    _    ___   _   _  ____",
        " / ___| | |  | |  / _ \ | | | |/ __ \\",
        "| |     | |  | | | | | || | | | |  | |",
        "| |     | |  | | | | | || | | | |  | |",
        "| |___  | |__| | | |_| || |_| | |__| |",
        " \____| \____/   \___/  \___/ \____/"
    ]

    return "\n".join(claude_art)


def main():
    """
    Main function to demonstrate ASCII art rendering.
    """
    print(render_claude_ascii_art())


if __name__ == "__main__":
    main()