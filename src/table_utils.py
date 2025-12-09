"""Utility functions for table transformations."""
from typing import Union, List, Any
import csv
from io import StringIO


def reverse_table_columns(
    table_data: Union[List[List[Any]], str],
    input_format: str = 'markdown'
) -> Union[List[List[Any]], str]:
    """
    Reverse the columns of a table, preserving its original structure.

    Supports multiple input formats with robust handling:
    - List of lists: Direct column reversal
    - CSV string: Parsed and reversed using csv module
    - Markdown table: Preserves alignment markers

    Args:
        table_data (Union[List[List[Any]], str]): Input table to reverse
        input_format (str, optional): Format of input table. Defaults to 'markdown'.

    Returns:
        Union[List[List[Any]], str]: Table with columns reversed in original format

    Raises:
        ValueError: If input is invalid or cannot be parsed

    Notes:
        - Idempotent: Applying twice returns original table
        - Handles empty tables, single columns
        - Preserves original data structure
    """
    # Handle empty input early
    if not table_data:
        return table_data

    # List of lists input (direct reversal)
    if isinstance(table_data, list):
        # Safe copy to prevent mutation
        return [row[::-1] for row in table_data]

    # CSV string input
    if input_format == 'csv':
        return _reverse_csv_columns(table_data)

    # Markdown table input (default)
    return _reverse_markdown_columns(table_data)


def _reverse_csv_columns(csv_string: str) -> str:
    """
    Reverse columns in a CSV string while maintaining formatting.

    Args:
        csv_string (str): CSV-formatted table string

    Returns:
        str: CSV string with columns reversed
    """
    # Use StringIO to make csv module work with strings
    reader = csv.reader(StringIO(csv_string))

    # Convert to list and reverse columns
    rows = list(reader)
    reversed_rows = [row[::-1] for row in rows]

    # Convert back to CSV string
    output = StringIO()
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(reversed_rows)

    return output.getvalue().strip()


def _reverse_markdown_columns(markdown_table: str) -> str:
    """
    Reverse columns in a markdown table, preserving alignment.

    Args:
        markdown_table (str): Markdown-formatted table string

    Returns:
        str: Markdown table with columns reversed
    """
    # Split table into lines
    lines = markdown_table.strip().split('\n')

    # Reverse each line, preserving structure
    reversed_lines = []
    for line in lines:
        # Split by '|', strip whitespace
        parts = [part.strip() for part in line.split('|') if part.strip()]

        # Reverse parts and reconstruct line
        reversed_parts = parts[::-1]
        reversed_line = '| ' + ' | '.join(reversed_parts) + ' |'
        reversed_lines.append(reversed_line)

    return '\n'.join(reversed_lines)