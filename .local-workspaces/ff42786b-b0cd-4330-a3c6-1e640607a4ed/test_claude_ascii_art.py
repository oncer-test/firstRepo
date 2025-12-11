"""Unit tests for Claude ASCII Art module."""
import unittest
from claude_ascii_art import validate_ascii_art, print_claude_ascii_art

class TestClaudeAsciiArt(unittest.TestCase):
    def test_valid_ascii_art(self):
        """Test that the Claude ASCII art passes validation."""
        art = """ _____  _    _    ___   _   _  ____
/ ____|| |  | |  / _ \ | | | |/ __ \\
| |    | |  | | | | | || | | | |  | |
| |    | |  | | | | | || | | | |  | |
| |____| |__| | | |_| || |_| | |__| |
 \\_____|\____/   \___/  \___/ \____/"""
        self.assertTrue(validate_ascii_art(art))

    def test_width_constraint(self):
        """Test width constraint validation."""
        too_wide = "x" * 41
        self.assertFalse(validate_ascii_art(too_wide))

    def test_height_constraint(self):
        """Test height constraint validation."""
        too_tall = "\n".join(["x" * 10] * 7)
        self.assertFalse(validate_ascii_art(too_tall))

    def test_print_claude_ascii_art(self):
        """Test that print_claude_ascii_art returns valid art."""
        art = print_claude_ascii_art()
        self.assertTrue(validate_ascii_art(art))

if __name__ == '__main__':
    unittest.main()