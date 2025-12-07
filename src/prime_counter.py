"""
Prime number counter module.

This module provides functions to count prime numbers before a given number.
It implements two approaches: basic iteration and the Sieve of Eratosthenes.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: Integer to check for primality

    Returns:
        Boolean indicating if n is prime
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def count_primes_before(n):
    """
    Count all prime numbers before a given number using basic iteration.

    Args:
        n: The upper limit (exclusive) for counting primes

    Returns:
        Count of prime numbers less than n

    Time Complexity: O(n * sqrt(n))
    Space Complexity: O(1)
    """
    if n <= 2:
        return 0

    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count


def sieve_of_eratosthenes(n):
    """
    Count all prime numbers before a given number using the Sieve of Eratosthenes.

    Args:
        n: The upper limit (exclusive) for counting primes

    Returns:
        Count of prime numbers less than n

    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return 0

    # Create a boolean array to track primes
    is_prime_arr = [True] * n
    is_prime_arr[0] = is_prime_arr[1] = False

    # Mark multiples of each prime as non-prime
    p = 2
    while p * p < n:
        if is_prime_arr[p]:
            # Mark all multiples of p as non-prime
            for i in range(p * p, n, p):
                is_prime_arr[i] = False
        p += 1

    # Count remaining primes
    return sum(is_prime_arr)


def get_primes_before(n):
    """
    Get a list of all prime numbers before a given number.

    Args:
        n: The upper limit (exclusive)

    Returns:
        List of prime numbers less than n
    """
    if n <= 2:
        return []

    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes
