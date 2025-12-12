"""Test suite for print_claude module."""
import io
import pytest

from src.ascii_art.print_claude import print_claude_art, CLAUDE_ASCII_ART


def test_print_claude_art_defaults():
    """Test default printing behavior."""
    output = io.StringIO()
    print_claude_art(file=output)
    assert output.getvalue().strip() == CLAUDE_ASCII_ART.strip()


def test_print_claude_art_custom():
    """Test custom ASCII art printing."""
    custom_art = """  CUSTOM
  ASCII
   ART    """
    output = io.StringIO()
    print_claude_art(art=custom_art, file=output)
    assert output.getvalue().strip() == custom_art.strip()


def test_print_claude_art_invalid():
    """Test invalid art handling."""
    with pytest.raises(ValueError, match="Invalid ASCII art"):
        print_claude_art(art="")  # Empty string

    with pytest.raises(ValueError, match="Invalid ASCII art"):
        print_claude_art(art="😀")  # Non-ASCII characters