# Claude ASCII Art

Simple, safe ASCII art rendering module.

## Features

- Safe rendering of Claude ASCII art
- Monospace-friendly design
- Secure validation mechanisms
- Flexible output streaming

## Usage

```python
from src.ascii_art.claude import render_claude_art, CLAUDE_ASCII_ART

# Display Claude ASCII art
render_claude_art(CLAUDE_ASCII_ART)

# Render to a file
with open('claude.txt', 'w') as f:
    render_claude_art(file=f)
```

## Design Constraints

- Maximum height: 6 lines
- Maximum width: 40 characters
- ASCII-only characters

## Testing

Run tests with pytest:

```bash
python3 -m pytest tests/
```