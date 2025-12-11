"""
Test module for Claude ASCII Art validation and rendering.
"""

import unittest
from claude_ascii_art import validate_ascii_art, render_claude_ascii_art, AsciiArtValidationError


class TestClaudeAsciiArt(unittest.TestCase):
    """Test suite for Claude ASCII Art module."""

    def test_valid_ascii_art(self):
        """Verify that valid ASCII art passes validation."""
        claude_ascii_art = [
            " _____  _    _   _      _   _  ____",
            "/ ____|| |  | | | |    | | | |/ __ \\",
            "| |    | |  | | | |    | | | | |  | |",
            "| |    | |  | | | |    | | | | |  | |",
            "| |____| |__| | | |____| |_| | |__| |",
            " \\_____|\____/  |______\\___/ \\____/"
        ]
        try:
            validate_ascii_art(claude_ascii_art)
        except AsciiArtValidationError:
            self.fail("Valid ASCII art raised unexpected validation error")

    def test_too_many_lines(self):
        """Verify error when too many lines are provided."""
        invalid_art = [
            "Line 1", "Line 2", "Line 3", "Line 4",
            "Line 5", "Line 6", "Line 7"
        ]
        with self.assertRaises(AsciiArtValidationError):
            validate_ascii_art(invalid_art)

    def test_line_too_long(self):
        """Verify error when line exceeds 40 characters."""
        invalid_art = [
            "A" * 41,
            "Line 2", "Line 3", "Line 4", "Line 5", "Line 6"
        ]
        with self.assertRaises(AsciiArtValidationError):
            validate_ascii_art(invalid_art)

    def test_non_ascii_characters(self):
        """Verify error when non-ASCII characters are used."""
        invalid_art = [
            "Valid Line",
            "Line with 🤖 emoji",
            "Line 3", "Line 4", "Line 5", "Line 6"
        ]
        with self.assertRaises(AsciiArtValidationError):
            validate_ascii_art(invalid_art)

    def test_render_claude_ascii_art(self):
        """Verify ASCII art is rendered correctly."""
        art = render_claude_ascii_art()
        lines = art.split('\n')
        self.assertEqual(len(lines), 6)
        self.assertTrue(all(len(line) <= 40 for line in lines))


if __name__ == '__main__':
    unittest.main()