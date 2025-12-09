"""
Utility functions for table transformations with robust input handling.

Key features:
- Idempotent column reversal
- Support for multiple table formats
- Comprehensive input validation
"""

from typing import List, Union, Any
import csv
from io import StringIO


class TableTransformationError(ValueError):
    """Custom exception for table transformation errors."""
    pass


def reverse_table_columns(
    table: Union[List[List[Any]], str],
    input_type: str = 'list'
) -> Union[List[List[Any]], str]:
    """
    Reverse table columns while preserving structure and ensuring idempotence.

    Args:
        table (Union[List[List[Any]], str]): Input table to reverse
        input_type (str): Type of input ('list', 'csv', 'markdown')

    Returns:
        Union[List[List[Any]], str]: Table with columns reversed

    Raises:
        TableTransformationError: For invalid input or transformation issues
    """
    # Validate input
    if not table:
        raise TableTransformationError("Cannot reverse empty table")

    # Handle different input types
    if input_type == 'list':
        if not isinstance(table, list):
            raise TableTransformationError("Invalid input: expected list")
        return [list(reversed(row)) for row in table]

    elif input_type == 'csv':
        # Use CSV parsing for robust handling
        try:
            csv_input = StringIO(table) if isinstance(table, str) else table
            reader = csv.reader(csv_input if isinstance(csv_input, StringIO) else StringIO(csv_input))
            rows = list(reader)

            # Reverse each row
            reversed_rows = [list(reversed(row)) for row in rows]

            # Regenerate CSV output
            output = StringIO()
            csv.writer(output).writerows(reversed_rows)
            return output.getvalue()
        except Exception as e:
            raise TableTransformationError(f"CSV transformation failed: {e}")

    elif input_type == 'markdown':
        # Handle markdown table parsing and transformation
        def _split_markdown_row(row: str) -> List[str]:
            """Split markdown row, handling pipe-separated cells."""
            return [cell.strip() for cell in row.strip('|').split('|')]

        # Split input into rows
        rows = table.strip().split('\n')
        if not rows:
            raise TableTransformationError("Empty markdown table")

        # Parse and reverse each row, preserving markdown formatting
        try:
            parsed_rows = [_split_markdown_row(row) for row in rows]
            reversed_rows = [list(reversed(row)) for row in parsed_rows]

            # Regenerate markdown table
            return '\n'.join(['|' + '|'.join(row) + '|' for row in reversed_rows])
        except Exception as e:
            raise TableTransformationError(f"Markdown transformation failed: {e}")

    else:
        raise TableTransformationError(f"Unsupported input type: {input_type}")