"""
Tests for Claude ASCII Art module.
"""

import io
import pytest
from src.ascii_art.claude import validate_ascii_art, render_claude_art, CLAUDE_ASCII_ART

def test_ascii_art_validation():
    """Test ASCII art validation function."""
    assert validate_ascii_art(CLAUDE_ASCII_ART)

    with pytest.raises(ValueError):
        validate_ascii_art("")

    with pytest.raises(ValueError):
        validate_ascii_art(None)

    # Height constraint
    with pytest.raises(ValueError):
        validate_ascii_art("\n".join(["a"] * 7))

    # Width constraint
    with pytest.raises(ValueError):
        validate_ascii_art("\n".join(["a" * 41]))

    # Check line length
    assert len(max(CLAUDE_ASCII_ART.splitlines(), key=len)) <= 40

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