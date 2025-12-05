#!/usr/bin/env python3
"""
Fibonacci Number Computation Module

This module provides two implementations for computing Fibonacci numbers:
1. Iterative: O(n) time, O(1) space - memory efficient
2. Memoized: O(n) time, O(n) space - cached results for fast repeated calls

Usage:
    python fib.py 10                              # Default: iterative
    python fib.py --method iterative 10           # Explicit iterative
    python fib.py --method memoized 10            # Using memoization
    python fib.py --method memoized 15 20         # Memoized, multiple calls

Examples:
    >>> fib_iterative(5)
    5
    >>> fib_memoized(10)
    55
"""

import sys
from typing import Dict


def fib_iterative(n: int) -> int:
    """
    Compute the nth Fibonacci number using iteration.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative

    Examples:
        >>> fib_iterative(0)
        0
        >>> fib_iterative(1)
        1
        >>> fib_iterative(5)
        5
        >>> fib_iterative(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def fib_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Compute the nth Fibonacci number using memoization (recursive with caching).

    Time Complexity: O(n)
    Space Complexity: O(n) - for memoization cache

    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        memo: Internal memoization dictionary (used for recursion)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative

    Examples:
        >>> fib_memoized(0)
        0
        >>> fib_memoized(1)
        1
        >>> fib_memoized(5)
        5
        >>> fib_memoized(10)
        55
    """
    if memo is None:
        memo = {}

    if n < 0:
        raise ValueError("n must be non-negative")

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


def main():
    """CLI interface for Fibonacci computation."""
    # Parse arguments
    method = "iterative"
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: python fib.py [--method iterative|memoized] <n> [n2 n3 ...]")
        print("\nExamples:")
        print("  python fib.py 10")
        print("  python fib.py --method iterative 10")
        print("  python fib.py --method memoized 10")
        print("  python fib.py --method memoized 15 20 25")
        sys.exit(1)

    # Check for method flag
    if args[0] == "--method":
        if len(args) < 3:
            print("Error: --method requires argument and at least one position")
            sys.exit(1)
        method = args[1]
        args = args[2:]

    if method not in ("iterative", "memoized"):
        print(f"Error: method must be 'iterative' or 'memoized', got '{method}'")
        sys.exit(1)

    # Select function
    fib_func = fib_iterative if method == "iterative" else fib_memoized

    # Compute Fibonacci for each argument
    try:
        for arg in args:
            n = int(arg)
            result = fib_func(n)
            print(f"fib({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
