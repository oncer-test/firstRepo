"""Unit tests for utility functions."""

import sys
import unittest

# Add src directory to path for imports
sys.path.insert(0, "../src")

from utils import validate_input, format_output


class TestValidateInput(unittest.TestCase):
    """Test the validate_input function."""

    def test_valid_integer_string(self):
        """Valid integer strings are parsed correctly."""
        is_valid, value, error = validate_input("10")
        self.assertTrue(is_valid)
        self.assertEqual(value, 10)
        self.assertIsNone(error)

    def test_valid_integer(self):
        """Valid integers are accepted."""
        is_valid, value, error = validate_input(42)
        self.assertTrue(is_valid)
        self.assertEqual(value, 42)
        self.assertIsNone(error)

    def test_zero(self):
        """Zero is valid."""
        is_valid, value, error = validate_input("0")
        self.assertTrue(is_valid)
        self.assertEqual(value, 0)
        self.assertIsNone(error)

    def test_negative_number(self):
        """Negative numbers are invalid."""
        is_valid, value, error = validate_input("-5")
        self.assertFalse(is_valid)
        self.assertIsNone(value)
        self.assertIn("non-negative", error)

    def test_invalid_string(self):
        """Non-numeric strings are invalid."""
        is_valid, value, error = validate_input("abc")
        self.assertFalse(is_valid)
        self.assertIsNone(value)
        self.assertIn("not a valid integer", error)

    def test_float_string(self):
        """Float strings are invalid."""
        is_valid, value, error = validate_input("3.14")
        self.assertFalse(is_valid)
        self.assertIsNone(value)

    def test_empty_string(self):
        """Empty strings are invalid."""
        is_valid, value, error = validate_input("")
        self.assertFalse(is_valid)
        self.assertIsNone(value)


class TestFormatOutput(unittest.TestCase):
    """Test the format_output function."""

    def test_basic_output(self):
        """Basic output with count and number."""
        output = format_output(4, 10)
        self.assertIn("Found 4 prime numbers before 10", output)

    def test_output_with_primes_short_list(self):
        """Output with primes list when list is short."""
        primes = [2, 3, 5, 7]
        output = format_output(4, 10, primes=primes)
        self.assertIn("Found 4 prime numbers before 10", output)
        self.assertIn("[2, 3, 5, 7]", output)

    def test_output_with_primes_long_list(self):
        """Output with first/last primes when list is long."""
        # Create a list with 101 items to trigger the first/last format
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547]  # 101 primes
        output = format_output(101, 560, primes=primes)
        self.assertIn("First 10 primes:", output)
        self.assertIn("Last 10 primes:", output)

    def test_output_with_timing(self):
        """Output includes execution time."""
        output = format_output(4, 10, elapsed_time=0.001234)
        self.assertIn("Execution time: 0.001234 seconds", output)

    def test_output_with_all_options(self):
        """Output with all options."""
        primes = [2, 3, 5, 7]
        output = format_output(4, 10, primes=primes, elapsed_time=0.001)
        self.assertIn("Found 4 prime numbers before 10", output)
        self.assertIn("[2, 3, 5, 7]", output)
        self.assertIn("Execution time: 0.001000 seconds", output)


if __name__ == "__main__":
    unittest.main()
