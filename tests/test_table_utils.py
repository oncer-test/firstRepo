"""Tests for table transformation utilities."""
import pytest
from src.table_utils import reverse_table_columns


def test_list_table_reversal():
    """Test column reversal for list-based tables."""
    input_table = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]
    assert reverse_table_columns(input_table) == expected


def test_csv_table_reversal():
    """Test column reversal for CSV-formatted tables."""
    input_csv = "a,b,c\n1,2,3\n4,5,6"
    expected_csv = "c,b,a\n3,2,1\n6,5,4"
    assert reverse_table_columns(input_csv, input_format='csv') == expected_csv


def test_markdown_table_reversal():
    """Test column reversal for markdown-formatted tables."""
    input_markdown = (
        "| a | b | c |\n"
        "|---|---|---|\n"
        "| 1 | 2 | 3 |\n"
        "| 4 | 5 | 6 |"
    )
    expected_markdown = (
        "| c | b | a |\n"
        "|---|---|---|\n"
        "| 3 | 2 | 1 |\n"
        "| 6 | 5 | 4 |"
    )
    assert reverse_table_columns(input_markdown, input_format='markdown') == expected_markdown


def test_idempotence():
    """Verify that applying reversal twice returns original table."""
    test_cases = [
        [[1, 2, 3], [4, 5, 6]],
        "a,b,c\n1,2,3\n4,5,6",
        "| a | b | c |\n|---|---|---|\n| 1 | 2 | 3 |"
    ]

    for case in test_cases:
        # Apply reversal twice
        first_reversal = reverse_table_columns(case)
        second_reversal = reverse_table_columns(first_reversal)

        # Check that second reversal matches original
        assert second_reversal == case


def test_empty_input():
    """Test handling of empty inputs."""
    assert reverse_table_columns([]) == []
    assert reverse_table_columns('') == ''
    assert reverse_table_columns('a,b,c\n', input_format='csv') == 'a,b,c\n'


def test_single_column_table():
    """Test reversal of single-column tables."""
    input_list = [[1], [2], [3]]
    assert reverse_table_columns(input_list) == input_list

    input_csv = "a\n1\n2\n3"
    assert reverse_table_columns(input_csv, input_format='csv') == input_csv

    input_markdown = "| a |\n|---|\n| 1 |\n| 2 |"
    assert reverse_table_columns(input_markdown, input_format='markdown') == input_markdown


def test_uneven_row_length():
    """Test handling of tables with uneven row lengths."""
    input_table = [[1, 2], [3, 4, 5], [6]]
    expected = [[2, 1], [5, 4, 3], [None, 6]]
    assert reverse_table_columns(input_table) == expected