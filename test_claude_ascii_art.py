"""
Test suite for Claude ASCII Art module
"""

import unittest
from claude_ascii_art import validate_ascii_art, render_claude_ascii_art


class TestClaudeAsciiArt(unittest.TestCase):
    def test_render_claude_ascii_art(self):
        """Test the default ASCII art rendering"""
        art = render_claude_ascii_art().split("\n")
        self.assertEqual(len(art), 6)
        self.assertTrue(all(len(line) <= 40 for line in art))

    def test_validate_ascii_art(self):
        """Test ASCII art validation constraints"""
        valid_art = [
            " _____  _    _    ___   _   _  ____",
            "/ ____|| |  | |  / _ \ | | | |/ __ \\",
        ]
        invalid_art_long_width = [
            " " * 41 + "x"
        ]
        invalid_art_long_height = [
            "x\n" * 7
        ]
        invalid_art_non_ascii = [
            "😊 Claude Art"
        ]

        self.assertIsNotNone(validate_ascii_art(valid_art))
        self.assertIsNone(validate_ascii_art(invalid_art_long_width))
        self.assertIsNone(validate_ascii_art(invalid_art_long_height))
        self.assertIsNone(validate_ascii_art(invalid_art_non_ascii))


if __name__ == "__main__":
    unittest.main()