#!/usr/bin/env python3
"""
Simple script to print Claude ASCII art.
"""

from src.ascii_art.claude import render_claude_art, CLAUDE_ASCII_ART

def main():
    """Print Claude ASCII art to console."""
    render_claude_art(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    main()