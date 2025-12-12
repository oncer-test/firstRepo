# Changelog

## [0.1.1] - 2025-12-11

### Added
- Comprehensive validation for ASCII art with detailed error messages
- New constraints for line width (max 40 chars) and height (max 6 lines)
- Enhanced test coverage for validation scenarios

### Changed
- Improved `validate_ascii_art()` to return tuple with validation status and error message
- Updated error handling in `render_claude_art()` to provide more context
- Expanded test suite with additional validation test cases

### Fixed
- Potential silent validation failures
- Inconsistent error handling in validation functions

## [0.1.0] - Initial Release
- Initial implementation of Claude ASCII art module