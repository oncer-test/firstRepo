"""Unit tests for prime counter module."""

import sys
import unittest

# Add src directory to path for imports
sys.path.insert(0, "../src")

from prime_counter import is_prime, count_primes_before, sieve_of_eratosthenes, get_primes_before


class TestIsPrime(unittest.TestCase):
    """Test the is_prime function."""

    def test_negative_numbers(self):
        """Negative numbers are not prime."""
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-1))

    def test_zero_and_one(self):
        """Zero and one are not prime."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_two_is_prime(self):
        """Two is prime."""
        self.assertTrue(is_prime(2))

    def test_even_numbers(self):
        """Even numbers greater than 2 are not prime."""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(100))

    def test_small_primes(self):
        """Test known small prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in primes:
            self.assertTrue(is_prime(p), f"{p} should be prime")

    def test_small_composites(self):
        """Test known non-prime numbers."""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for c in composites:
            self.assertFalse(is_prime(c), f"{c} should not be prime")

    def test_large_prime(self):
        """Test a larger prime number."""
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))

    def test_large_composite(self):
        """Test a larger composite number."""
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(121))  # 11 * 11


class TestCountPrimesBefore(unittest.TestCase):
    """Test the count_primes_before function."""

    def test_zero(self):
        """Count of primes before 0 is 0."""
        self.assertEqual(count_primes_before(0), 0)

    def test_one(self):
        """Count of primes before 1 is 0."""
        self.assertEqual(count_primes_before(1), 0)

    def test_two(self):
        """Count of primes before 2 is 0."""
        self.assertEqual(count_primes_before(2), 0)

    def test_three(self):
        """Count of primes before 3 is 1 (only 2)."""
        self.assertEqual(count_primes_before(3), 1)

    def test_ten(self):
        """Count of primes before 10 is 4 (2, 3, 5, 7)."""
        self.assertEqual(count_primes_before(10), 4)

    def test_twenty(self):
        """Count of primes before 20 is 8 (2, 3, 5, 7, 11, 13, 17, 19)."""
        self.assertEqual(count_primes_before(20), 8)

    def test_hundred(self):
        """Count of primes before 100 is 25."""
        self.assertEqual(count_primes_before(100), 25)

    def test_thousand(self):
        """Count of primes before 1000 is 168."""
        self.assertEqual(count_primes_before(1000), 168)


class TestSieveOfEratosthenes(unittest.TestCase):
    """Test the sieve_of_eratosthenes function."""

    def test_zero(self):
        """Count of primes before 0 is 0."""
        self.assertEqual(sieve_of_eratosthenes(0), 0)

    def test_one(self):
        """Count of primes before 1 is 0."""
        self.assertEqual(sieve_of_eratosthenes(1), 0)

    def test_two(self):
        """Count of primes before 2 is 0."""
        self.assertEqual(sieve_of_eratosthenes(2), 0)

    def test_three(self):
        """Count of primes before 3 is 1."""
        self.assertEqual(sieve_of_eratosthenes(3), 1)

    def test_ten(self):
        """Count of primes before 10 is 4."""
        self.assertEqual(sieve_of_eratosthenes(10), 4)

    def test_twenty(self):
        """Count of primes before 20 is 8."""
        self.assertEqual(sieve_of_eratosthenes(20), 8)

    def test_hundred(self):
        """Count of primes before 100 is 25."""
        self.assertEqual(sieve_of_eratosthenes(100), 25)

    def test_thousand(self):
        """Count of primes before 1000 is 168."""
        self.assertEqual(sieve_of_eratosthenes(1000), 168)

    def test_consistency_with_basic(self):
        """Sieve results match basic iteration for various inputs."""
        test_values = [10, 20, 50, 100, 200]
        for n in test_values:
            basic_count = count_primes_before(n)
            sieve_count = sieve_of_eratosthenes(n)
            self.assertEqual(
                basic_count,
                sieve_count,
                f"Count mismatch at n={n}: basic={basic_count}, sieve={sieve_count}",
            )


class TestGetPrimesBefore(unittest.TestCase):
    """Test the get_primes_before function."""

    def test_two(self):
        """Get primes before 2 returns empty list."""
        self.assertEqual(get_primes_before(2), [])

    def test_three(self):
        """Get primes before 3 returns [2]."""
        self.assertEqual(get_primes_before(3), [2])

    def test_ten(self):
        """Get primes before 10 returns [2, 3, 5, 7]."""
        self.assertEqual(get_primes_before(10), [2, 3, 5, 7])

    def test_twenty(self):
        """Get primes before 20 returns correct list."""
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(get_primes_before(20), expected)

    def test_hundred_count(self):
        """Get primes before 100 returns 25 primes."""
        primes = get_primes_before(100)
        self.assertEqual(len(primes), 25)

    def test_hundred_values(self):
        """Get primes before 100 returns correct values."""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(get_primes_before(100), expected)


if __name__ == "__main__":
    unittest.main()
