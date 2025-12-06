#!/usr/bin/env python3
"""
Fibonacci Number Computation Module

This module provides implementations for computing Fibonacci numbers with optional multiplication:
1. Iterative: O(n) time, O(1) space - memory efficient
2. Memoized: O(n) time, O(n) space - cached results for fast repeated calls
3. Multiplied variants: Multiply the Fibonacci number by a given factor

Usage:
    python fib.py 10                              # Default: iterative
    python fib.py --method iterative 10           # Explicit iterative
    python fib.py --method memoized 10            # Using memoization
    python fib.py --multiply 2 10                 # Iterative with multiplier
    python fib.py --method memoized --multiply 3 15 20  # Memoized with multiplier

Examples:
    >>> fib_iterative(5)
    5
    >>> fib_memoized(10)
    55
    >>> fib_multiplied_iterative(5, 2)
    10
    >>> fib_multiplied_memoized(10, 3)
    165
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


def fib_multiplied_iterative(n: int, multiplier: int) -> int:
    """
    Compute the nth Fibonacci number and multiply by a given factor using iteration.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        multiplier: The factor to multiply the Fibonacci number by

    Returns:
        The nth Fibonacci number multiplied by the multiplier

    Raises:
        ValueError: If n is negative or multiplier is not positive

    Examples:
        >>> fib_multiplied_iterative(0, 2)
        0
        >>> fib_multiplied_iterative(1, 2)
        2
        >>> fib_multiplied_iterative(5, 2)
        10
        >>> fib_multiplied_iterative(10, 3)
        165
    """
    if multiplier <= 0:
        raise ValueError("multiplier must be positive")

    return fib_iterative(n) * multiplier


def fib_multiplied_memoized(n: int, multiplier: int, memo: Dict[int, int] = None) -> int:
    """
    Compute the nth Fibonacci number and multiply by a given factor using memoization.

    Time Complexity: O(n)
    Space Complexity: O(n) - for memoization cache

    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        multiplier: The factor to multiply the Fibonacci number by
        memo: Internal memoization dictionary (used for recursion)

    Returns:
        The nth Fibonacci number multiplied by the multiplier

    Raises:
        ValueError: If n is negative or multiplier is not positive

    Examples:
        >>> fib_multiplied_memoized(0, 2)
        0
        >>> fib_multiplied_memoized(1, 2)
        2
        >>> fib_multiplied_memoized(5, 2)
        10
        >>> fib_multiplied_memoized(10, 3)
        165
    """
    if multiplier <= 0:
        raise ValueError("multiplier must be positive")

    return fib_memoized(n, memo) * multiplier


def main():
    """CLI interface for Fibonacci computation."""
    method = "iterative"
    multiplier = 1
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: python fib.py [--method iterative|memoized] [--multiply <factor>] <n> [n2 n3 ...]")
        print("\nExamples:")
        print("  python fib.py 10")
        print("  python fib.py --method iterative 10")
        print("  python fib.py --method memoized 10")
        print("  python fib.py --multiply 2 10")
        print("  python fib.py --method memoized --multiply 3 15 20")
        sys.exit(1)

    # Parse flags
    while args and args[0].startswith("--"):
        flag = args.pop(0)
        if flag == "--method":
            if not args:
                print("Error: --method requires an argument")
                sys.exit(1)
            method = args.pop(0)
        elif flag == "--multiply":
            if not args:
                print("Error: --multiply requires an argument")
                sys.exit(1)
            try:
                multiplier = int(args.pop(0))
            except ValueError:
                print("Error: --multiply argument must be an integer")
                sys.exit(1)
        else:
            print(f"Error: unknown flag '{flag}'")
            sys.exit(1)

    if not args:
        print("Error: at least one position argument required")
        sys.exit(1)

    if method not in ("iterative", "memoized"):
        print(f"Error: method must be 'iterative' or 'memoized', got '{method}'")
        sys.exit(1)

    # Select function based on method and multiplier
    if multiplier != 1:
        fib_func = fib_multiplied_iterative if method == "iterative" else fib_multiplied_memoized
        use_multiplier = True
    else:
        fib_func = fib_iterative if method == "iterative" else fib_memoized
        use_multiplier = False

    # Compute Fibonacci for each argument
    try:
        for arg in args:
            n = int(arg)
            if use_multiplier:
                result = fib_func(n, multiplier)
            else:
                result = fib_func(n)

            if multiplier != 1:
                print(f"fib({n}) * {multiplier} = {result}")
            else:
                print(f"fib({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
