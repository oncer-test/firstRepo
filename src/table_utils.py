"""
Utility functions for tabular data transformations.

This module provides tools for manipulating tabular data structures,
with a focus on safety, performance, and flexibility.
"""

from typing import List, Union, Literal, Any
import csv
import io

def reverse_table_columns(
    table_data: Union[List[List[Any]], str],
    input_format: Literal['csv', 'markdown'] = 'markdown'
) -> Union[List[List[Any]], str]:
    """
    Reverse the order of columns in a table from right to left.

    Ensures idempotence: applying the function twice returns the original data.
    Supports both list-of-lists and string-based table formats.

    Args:
        table_data: Table to be reversed. Can be list of lists or CSV/markdown string.
        input_format: Format of the input table ('csv' or 'markdown').

    Returns:
        Table with columns reversed in the same format as input.

    Raises:
        ValueError: For invalid input formats or empty tables.
        TypeError: For unsupported input types.

    Examples:
        >>> reverse_table_columns([['a', 'b', 'c'], [1, 2, 3]])
        [['c', 'b', 'a'], [3, 2, 1]]
        >>> reverse_table_columns('a,b,c\\n1,2,3', input_format='csv')
        'c,b,a\\n3,2,1'
    """
    # Handle empty or invalid input
    if not table_data:
        raise ValueError("Cannot reverse empty table")

    # Handle string inputs
    if isinstance(table_data, str):
        if input_format == 'csv':
            return _reverse_csv_columns(table_data)
        elif input_format == 'markdown':
            return _reverse_markdown_columns(table_data)
        else:
            raise ValueError(f"Unsupported input format: {input_format}")

    # Handle list-of-lists input
    if not isinstance(table_data, list):
        raise TypeError(f"Unsupported input type: {type(table_data)}")

    # Ensure all rows have same length, pad if needed
    max_row_length = max(len(row) for row in table_data)
    normalized_table = [
        row + [None] * (max_row_length - len(row))
        for row in table_data
    ]

    # Reverse columns
    return [
        [row[col] for col in range(len(row)-1, -1, -1)]
        for row in normalized_table
    ]

def _reverse_csv_columns(csv_data: str) -> str:
    """
    Reverse columns in a CSV string.

    Preserves CSV formatting, handles header rows.
    """
    # Use csv module for robust parsing
    csv_reader = csv.reader(io.StringIO(csv_data))
    rows = list(csv_reader)

    # Reverse the columns
    reversed_rows = [row[::-1] for row in rows]

    # Convert back to CSV string
    output = io.StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerows(reversed_rows)

    return output.getvalue().strip()

def _reverse_markdown_columns(markdown_data: str) -> str:
    """
    Reverse columns in a markdown table.

    Handles markdown table formatting, including alignment rows.
    """
    # Split into lines
    lines = markdown_data.strip().split('\n')

    # Reverse each line
    reversed_lines = [
        '|' + '|'.join(line.strip('|').split('|')[::-1]) + '|'
        for line in lines
    ]

    return '\n'.join(reversed_lines)