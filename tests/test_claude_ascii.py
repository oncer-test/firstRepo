"""
Tests for Claude ASCII Art module.
"""

import io
import pytest
from src.ascii_art.claude import validate_ascii_art, render_claude_art, CLAUDE_ASCII_ART

def test_ascii_art_validation():
    """Test ASCII art validation function."""
    assert validate_ascii_art(CLAUDE_ASCII_ART)
    assert not validate_ascii_art("")
    assert not validate_ascii_art(None)
    assert not validate_ascii_art("x" * 2000)  # Too long

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