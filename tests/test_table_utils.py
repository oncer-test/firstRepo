"""
Test suite for table column reversal utility.
"""

import pytest
from src.table_utils import reverse_table_columns, TableTransformationError


def test_list_column_reversal():
    """Test column reversal for list of lists."""
    input_table = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [3, 2, 1],
        [6, 5, 4]
    ]
    assert reverse_table_columns(input_table) == expected


def test_csv_column_reversal():
    """Test column reversal for CSV string."""
    input_csv = "a,b,c\n1,2,3\n4,5,6"
    result = reverse_table_columns(input_csv, input_type='csv')
    expected_csv = "c,b,a\n3,2,1\n6,5,4"
    assert result.strip() == expected_csv.strip()


def test_markdown_column_reversal():
    """Test column reversal for markdown table."""
    input_markdown = "| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |"
    result = reverse_table_columns(input_markdown, input_type='markdown')
    expected_markdown = "| c | b | a |\n| 3 | 2 | 1 |\n| 6 | 5 | 4 |"
    assert result.strip() == expected_markdown.strip()


def test_idempotence():
    """Verify that double reversal returns original table."""
    input_table = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    first_reversal = reverse_table_columns(input_table)
    second_reversal = reverse_table_columns(first_reversal)
    assert second_reversal == input_table


def test_empty_table_error():
    """Test error handling for empty tables."""
    with pytest.raises(TableTransformationError):
        reverse_table_columns([])


def test_unsupported_type_error():
    """Test error for unsupported input type."""
    with pytest.raises(TableTransformationError):
        reverse_table_columns("test", input_type='xml')