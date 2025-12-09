"""Utilities for tabular data transformations."""
from typing import List, Any, Union, Optional
import csv
from io import StringIO


def reverse_table_columns(
    table_data: Union[List[List[Any]], str],
    input_format: str = 'markdown'
) -> Union[List[List[Any]], str]:
    """
    Reverse the columns of a table from right to left.

    Ensures idempotence by applying the reversal transformation consistently.
    Supports markdown and CSV formatted tables.

    Args:
        table_data (Union[List[List[Any]], str]):
            Input table as list of lists or string representation.
        input_format (str, optional):
            Format of the input table. Defaults to 'markdown'.
            Supports 'markdown' and 'csv'.

    Returns:
        Union[List[List[Any]], str]:
            Table with columns reversed, preserving original structure.

    Raises:
        ValueError: If input is invalid or cannot be processed safely.

    Notes:
        - Idempotent: Applying twice returns original table
        - Handles empty tables, single-column tables
        - Preserves original formatting for markdown
    """
    # Validate input type and format
    if not table_data:
        return table_data  # Empty input returns empty result

    # Handle string (CSV or markdown) input
    if isinstance(table_data, str):
        if input_format == 'csv':
            return _reverse_csv_columns(table_data)
        elif input_format == 'markdown':
            return _reverse_markdown_columns(table_data)
        else:
            raise ValueError(f"Unsupported input format: {input_format}")

    # Handle list of lists
    if not isinstance(table_data, list):
        raise ValueError("Input must be list of lists or string")

    # Reverse columns for list-based tables
    max_row_len = max(len(row) for row in table_data)
    reversed_table = [
        list(reversed(row + [None] * (max_row_len - len(row))))
        for row in table_data
    ]

    return reversed_table


def _reverse_csv_columns(csv_data: str) -> str:
    """
    Reverse columns in a CSV-formatted string.

    Args:
        csv_data (str): CSV-formatted table string.

    Returns:
        str: CSV table with columns reversed.
    """
    # Use StringIO to handle CSV parsing
    input_csv = StringIO(csv_data)
    output_csv = StringIO()

    # Read and reverse CSV rows
    csv_reader = csv.reader(input_csv)
    csv_writer = csv.writer(output_csv)

    # Reverse each row
    reversed_rows = [list(reversed(row)) for row in csv_reader]
    csv_writer.writerows(reversed_rows)

    return output_csv.getvalue().strip()


def _reverse_markdown_columns(markdown_table: str) -> str:
    """
    Reverse columns in a markdown-formatted table.

    Args:
        markdown_table (str): Markdown table string.

    Returns:
        str: Markdown table with columns reversed.
    """
    # Split markdown table into lines
    lines = markdown_table.strip().split('\n')

    # Handle empty or single-line tables
    if len(lines) < 2:
        return markdown_table

    # Separate header and alignment rows if present
    header = lines[0].split('|')[1:-1]
    alignment = lines[1].split('|')[1:-1] if len(lines) > 1 else None
    data_lines = lines[2:] if alignment else lines[1:]

    # Reverse header and data rows
    reversed_header = list(reversed(header))
    reversed_data = [
        '|'.join([''] + list(reversed(row.split('|')[1:-1])) + [''])
        for row in data_lines
    ]

    # Reconstruct markdown table
    if alignment:
        reversed_alignment = list(reversed(alignment))
        result_lines = [
            '|' + '|'.join(reversed_header) + '|',
            '|' + '|'.join(reversed_alignment) + '|',
            *reversed_data
        ]
    else:
        result_lines = [
            '|' + '|'.join(reversed_header) + '|',
            *reversed_data
        ]

    return '\n'.join(result_lines)