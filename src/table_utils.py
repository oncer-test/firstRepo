"""
Utility functions for table column reversal and transformation.

Supports multiple input formats:
- Lists of lists
- CSV strings
- Markdown tables

Provides safe, non-mutating transformations with robust error handling.
"""

from typing import List, Union, Any
import csv
import io


class TableTransformationError(Exception):
    """Custom exception for table transformation errors."""
    pass


def reverse_table_columns(
    table: Union[List[List[Any]], str],
    input_type: str = 'list'
) -> Union[List[List[Any]], str]:
    """
    Reverse columns of a table from right to left.

    Idempotent operation that works with:
    - Lists of lists
    - CSV strings
    - Markdown tables

    Args:
        table: Input table data
        input_type: Format of input ('list', 'csv', 'markdown')

    Returns:
        Table with columns reversed

    Raises:
        TableTransformationError: For invalid input or unsupported formats
    """
    # Validate input
    if not table:
        raise TableTransformationError("Empty input table")

    # Convert input to list of lists for processing
    if isinstance(table, str):
        if input_type == 'csv':
            table = _reverse_csv_columns(table)
        elif input_type == 'markdown':
            table = _reverse_markdown_columns(table)
        else:
            raise TableTransformationError(f"Unsupported input type: {input_type}")
    elif isinstance(table, list):
        # Reverse columns by transposing and reversing
        if not table[0]:
            raise TableTransformationError("Cannot reverse empty table")

        # Pad rows to equal length to prevent index errors
        max_length = max(len(row) for row in table)
        padded_table = [row + [None] * (max_length - len(row)) for row in table]

        # Transpose, reverse, and transpose back
        reversed_table = list(map(list, zip(*padded_table)))[::-1]
        reversed_table = list(map(list, zip(*reversed_table)))

        # Remove None padding
        reversed_table = [
            [cell for cell in row if cell is not None]
            for row in reversed_table
        ]
        table = reversed_table
    else:
        raise TableTransformationError("Invalid input type")

    return table


def _reverse_csv_columns(csv_data: str) -> List[List[Any]]:
    """
    Reverse columns in a CSV string.

    Args:
        csv_data: Input CSV string

    Returns:
        List of lists with columns reversed
    """
    # Use StringIO to make CSV string file-like
    csv_reader = csv.reader(io.StringIO(csv_data))

    # Convert to list of lists and reverse columns
    table = list(csv_reader)
    reversed_table = list(map(list, zip(*table)))[::-1]

    # Convert back to CSV
    output = io.StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerows(reversed_table)

    return output.getvalue()


def _reverse_markdown_columns(markdown_data: str) -> str:
    """
    Reverse columns in a markdown table.

    Args:
        markdown_data: Input markdown table string

    Returns:
        Markdown table with columns reversed
    """
    # Split markdown table into rows
    rows = markdown_data.strip().split('\n')

    # Separate header and alignment rows if present
    header_row = rows[0]
    alignment_row = rows[1] if len(rows) > 1 and '---' in rows[1] else None
    data_rows = rows[2:] if alignment_row else rows[1:]

    # Parse rows into cells
    parsed_rows = [row.strip('|').split('|') for row in data_rows]
    parsed_rows = [[cell.strip() for cell in row] for row in parsed_rows]

    # Reverse columns, preserving original rows
    reversed_rows = list(map(list, zip(*parsed_rows)))[::-1]

    # Reconstruct markdown table
    reversed_markdown_rows = [
        '| ' + ' | '.join(row) + ' |'
        for row in reversed_rows
    ]

    # Add header and alignment row back if they existed
    if alignment_row:
        reversed_markdown_rows.insert(0, header_row)
        reversed_markdown_rows.insert(1, alignment_row)
    elif header_row:
        reversed_markdown_rows.insert(0, header_row)

    return '\n'.join(reversed_markdown_rows)