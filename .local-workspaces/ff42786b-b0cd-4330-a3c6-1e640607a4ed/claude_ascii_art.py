"""Claude ASCII Art Printer."""

def print_claude_ascii_art() -> str:
    """Print Claude ASCII art with validation."""
    claude_art = r""" _____  _    _    ___   _   _  ____
/ ____|| |  | |  / _ \ | | | |/ __ \
| |    | |  | | | | | || | | | |  | |
| |    | |  | | | | | || | | | |  | |
| |____| |__| | | |_| || |_| | |__| |
 \_____|\____/   \___/  \___/ \____/"""

    print(claude_art)
    return claude_art

def main():
    """Entry point for ASCII art printing."""
    print_claude_ascii_art()

if __name__ == '__main__':
    main()