"""Tests for table column reversal utility."""
import pytest
from src.table_utils import reverse_table_columns


def test_list_table_reversal():
    """Test reversing a list of lists."""
    input_table = [
        ['A', 'B', 'C'],
        ['1', '2', '3']
    ]
    expected = [
        ['C', 'B', 'A'],
        ['3', '2', '1']
    ]
    assert reverse_table_columns(input_table) == expected


def test_csv_table_reversal():
    """Test reversing CSV table."""
    input_csv = "A,B,C\n1,2,3"
    expected_csv = "C,B,A\n3,2,1"
    assert reverse_table_columns(input_csv, input_format='csv') == expected_csv


def test_markdown_table_reversal():
    """Test reversing markdown table with alignment."""
    input_markdown = (
        "| A | B | C |\n"
        "|---|---|---|\n"
        "| 1 | 2 | 3 |"
    )
    expected_markdown = (
        "| C | B | A |\n"
        "|---|---|---|\n"
        "| 3 | 2 | 1 |"
    )
    assert reverse_table_columns(input_markdown) == expected_markdown


def test_idempotence():
    """Verify idempotence: reversing twice returns original."""
    input_table = [['A', 'B'], ['1', '2']]
    first_reversal = reverse_table_columns(input_table)
    second_reversal = reverse_table_columns(first_reversal)
    assert second_reversal == input_table


def test_empty_input():
    """Test handling of empty input."""
    assert reverse_table_columns([]) == []
    assert reverse_table_columns('') == ''
    assert reverse_table_columns('', input_format='csv') == ''


def test_single_column_table():
    """Test single column table remains unchanged."""
    input_table = [['A'], ['1']]
    assert reverse_table_columns(input_table) == input_table