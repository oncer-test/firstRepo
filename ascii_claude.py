#!/usr/bin/env python3
"""
ASCII Art Display for Claude
Safe rendering of predefined ASCII art
"""

CLAUDE_ASCII_ART = r'''  _______ _        _        ______ _______
 |__   __| |      | |      |  ____|__   __|
    | |  | |      | |      | |__     | |
    | |  | |      | |      |  __|    | |
    | |  | |____  | |____  | |____   | |
    |_|  |______| |______| |______|  |_|   '''

def display_claude_art():
    """Safely display Claude ASCII art."""
    print(CLAUDE_ASCII_ART)

if __name__ == '__main__':
    display_claude_art()