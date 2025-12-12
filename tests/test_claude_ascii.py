"""Tests for Claude ASCII Art module."""

import io
import pytest
from src.ascii_art.claude import validate_ascii_art, render_claude_art, CLAUDE_ASCII_ART


def test_ascii_art_validation():
    """Test ASCII art validation function."""
    is_valid, _ = validate_ascii_art(CLAUDE_ASCII_ART)
    assert is_valid

    is_valid, error_msg = validate_ascii_art("")
    assert not is_valid
    assert "Art cannot be empty" in error_msg

    is_valid, error_msg = validate_ascii_art(None)
    assert not is_valid
    assert "Art cannot be None" in error_msg

    is_valid, error_msg = validate_ascii_art("x" * 2000)
    assert not is_valid
    assert "Art cannot exceed 1024 characters" in error_msg

    # Width check for existing art
    assert len(max(CLAUDE_ASCII_ART.splitlines(), key=len)) <= 40


def test_render_claude_art():
    """Test ASCII art rendering."""
    output = io.StringIO()
    render_claude_art(CLAUDE_ASCII_ART, file=output)
    rendered_art = output.getvalue()

    assert rendered_art.strip() == CLAUDE_ASCII_ART.strip()


def test_render_invalid_art():
    """Test rendering with invalid art raises an error."""
    with pytest.raises(ValueError, match="Invalid ASCII art"):
        render_claude_art("")


def test_line_height_validation():
    """Test that art cannot exceed 6 lines."""
    too_many_lines = "\n".join(["line"] * 7)
    is_valid, error_msg = validate_ascii_art(too_many_lines)

    assert not is_valid
    assert "Art cannot exceed 6 lines" in error_msg


def test_line_width_validation():
    """Test that lines cannot exceed 40 characters."""
    too_long_line = "a" * 41
    is_valid, error_msg = validate_ascii_art(too_long_line)

    assert not is_valid
    assert "Each line must be 40 characters or less" in error_msg