"""Main entry point for the prime number counter system."""

import argparse
import sys
import time
from prime_counter import count_primes_before, sieve_of_eratosthenes, get_primes_before
from utils import validate_input, format_output


def main():
    """Main function to parse arguments and run the prime counter."""
    parser = argparse.ArgumentParser(
        description="Count prime numbers before a given number",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py 10
  python main.py 100 --method sieve
  python main.py 1000 --method basic --show-primes
        """,
    )

    parser.add_argument(
        "number",
        type=str,
        help="The upper limit (exclusive) for counting primes",
    )
    parser.add_argument(
        "--method",
        choices=["basic", "sieve"],
        default="sieve",
        help="Algorithm to use for counting primes (default: sieve)",
    )
    parser.add_argument(
        "--show-primes",
        action="store_true",
        help="Display the list of primes found",
    )
    parser.add_argument(
        "--time",
        action="store_true",
        help="Display execution time",
    )

    args = parser.parse_args()

    # Validate input
    is_valid, n, error_msg = validate_input(args.number)
    if not is_valid:
        print(f"Error: {error_msg}", file=sys.stderr)
        sys.exit(1)

    # Measure execution time if requested
    start_time = time.time() if args.time else None

    # Count primes using selected method
    if args.method == "basic":
        count = count_primes_before(n)
    else:  # sieve
        count = sieve_of_eratosthenes(n)

    elapsed_time = time.time() - start_time if args.time else None

    # Get primes list if requested
    primes = get_primes_before(n) if args.show_primes else None

    # Format and display output
    output = format_output(count, n, primes, elapsed_time)
    print(output)


if __name__ == "__main__":
    main()
