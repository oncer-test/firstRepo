"""
Test suite for table column reversal utility.

Covers various input types, edge cases, and idempotence.
"""

import pytest
from src.table_utils import reverse_table_columns

def test_list_of_lists_reversal():
    """Test basic list of lists column reversal."""
    input_table = [['a', 'b', 'c'], [1, 2, 3]]
    expected = [['c', 'b', 'a'], [3, 2, 1]]
    assert reverse_table_columns(input_table) == expected

def test_csv_reversal():
    """Test CSV column reversal."""
    input_csv = 'a,b,c\n1,2,3'
    expected_csv = 'c,b,a\n3,2,1'
    assert reverse_table_columns(input_csv, input_format='csv') == expected_csv

def test_markdown_reversal():
    """Test markdown table column reversal."""
    input_markdown = '| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |'
    expected_markdown = '| c | b | a |\n|---|---|---|\n| 3 | 2 | 1 |'
    assert reverse_table_columns(input_markdown, input_format='markdown') == expected_markdown

def test_idempotence():
    """Verify that reversing columns twice returns original data."""
    original = [['a', 'b', 'c'], [1, 2, 3]]
    twice_reversed = reverse_table_columns(
        reverse_table_columns(original)
    )
    assert twice_reversed == original

def test_empty_table_raises_error():
    """Ensure empty tables raise a ValueError."""
    with pytest.raises(ValueError):
        reverse_table_columns([])
    with pytest.raises(ValueError):
        reverse_table_columns('')

def test_uneven_row_lengths():
    """Test handling of rows with different lengths."""
    input_table = [['a', 'b'], [1, 2, 3], ['x']]
    expected = [['b', 'a'], [3, 2, None], ['x', None]]
    assert reverse_table_columns(input_table) == expected

def test_single_column_table():
    """Verify behavior with single-column tables."""
    input_table = [['a'], [1], ['x']]
    assert reverse_table_columns(input_table) == input_table