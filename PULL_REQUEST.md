# Table Column Reversal Utility

## Overview
Implements a generic table column reversal function supporting multiple formats:
- List-of-lists
- CSV strings
- Markdown tables

## Changes
- Added `reverse_table_columns()` function in `src/table_utils.py`
- Created comprehensive test suite in `tests/test_table_utils.py`

### Key Features
- Handles different input types
- Supports CSV and markdown formats
- Preserves original data structure
- Robust error handling

### Known Limitations
- Does not support pandas DataFrame (planned future enhancement)
- Minimal handling of complex markdown table alignments

## Test Coverage
- 5/7 tests passing
- Covers basic reversal scenarios
- Handles edge cases like single-row/column tables

## Remaining Tasks
- Resolve uneven row handling semantics
- Normalize CSV line endings
- Enhance input validation
- Expand test coverage for edge cases

## Safety Considerations
- No in-place mutations
- Explicit type checking
- Minimal side effects

Fixes #TODO (reference issue number if applicable)