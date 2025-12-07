"""Utility functions for input validation and output formatting."""


def validate_input(value):
    """
    Validate that input is a positive integer.

    Args:
        value: Value to validate (can be string or int)

    Returns:
        Tuple of (is_valid, parsed_value, error_message)
    """
    try:
        num = int(value)
        if num < 0:
            return False, None, "Number must be non-negative"
        return True, num, None
    except (ValueError, TypeError):
        return False, None, f"Invalid input: '{value}' is not a valid integer"


def format_output(count, n, primes=None, elapsed_time=None):
    """
    Format the output for display.

    Args:
        count: Number of primes found
        n: The upper limit used
        primes: Optional list of the actual primes
        elapsed_time: Optional execution time in seconds

    Returns:
        Formatted string for display
    """
    output = f"Found {count} prime numbers before {n}"

    if primes and len(primes) <= 100:
        output += f"\nPrimes: {primes}"
    elif primes:
        output += f"\nFirst 10 primes: {primes[:10]}"
        output += f"\nLast 10 primes: {primes[-10:]}"

    if elapsed_time is not None:
        output += f"\nExecution time: {elapsed_time:.6f} seconds"

    return output
