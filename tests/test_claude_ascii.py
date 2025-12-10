"""
Tests for Claude ASCII Art module.
"""

import io
import pytest
from src.ascii_art.claude import validate_ascii_art, render_claude_art, CLAUDE_ASCII_ART

def test_ascii_art_validation():
    """Test ASCII art validation function."""
    max_len = max(len(line) for line in CLAUDE_ASCII_ART.splitlines())
    max_height = len(CLAUDE_ASCII_ART.splitlines())

    assert validate_ascii_art(CLAUDE_ASCII_ART)
    assert not validate_ascii_art("")
    assert not validate_ascii_art(None)
    assert not validate_ascii_art("x" * 2000)  # Too long

    # Explicit width and height checks
    assert validate_ascii_art(CLAUDE_ASCII_ART, max_width=max_len, max_height=max_height)
    assert not validate_ascii_art(CLAUDE_ASCII_ART, max_width=max_len-1)  # Too wide
    assert not validate_ascii_art(CLAUDE_ASCII_ART, max_height=max_height-1)  # Too tall

    # Non-ASCII art check
    assert not validate_ascii_art("こんにちは")  # Non-ASCII characters

def test_render_claude_art():
    """Test ASCII art rendering."""
    output = io.StringIO()
    render_claude_art(CLAUDE_ASCII_ART, file=output)
    rendered_art = output.getvalue()

    assert rendered_art.strip() == CLAUDE_ASCII_ART.strip()

def test_render_invalid_art():
    """Test rendering with invalid art raises an error."""
    with pytest.raises(ValueError):
        render_claude_art("")