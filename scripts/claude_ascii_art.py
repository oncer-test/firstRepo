#!/usr/bin/env python3
"""Safe ASCII art renderer for Claude logo."""

def render_claude_ascii_art() -> None:
    """Render the Claude ASCII art logo."""
    art = '''  ____ _       _   _   _    ____
 / ___| | __ _| |_| | | |  / ___|
| |   | |/ _` | __| | | | | |
| |___| | (_| | |_| |_| | | |___
 \\____|_|\\__,_|\\__|_(_)_|  \\____|'''
    print(art)

def main() -> None:
    """Main entry point for ASCII art rendering."""
    render_claude_ascii_art()

if __name__ == "__main__":
    main()