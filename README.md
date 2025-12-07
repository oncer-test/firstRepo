# Prime Number Counter System

A Python system that counts and analyzes prime numbers before a given number. This project implements multiple algorithms for prime counting with comprehensive testing and a user-friendly CLI interface.

## Features

- **Two Counting Algorithms**:
  - Basic iteration method: Simple, easy to understand (O(n√n) time)
  - Sieve of Eratosthenes: Fast and efficient for large ranges (O(n log log n) time)

- **Flexible CLI Interface**:
  - Specify any positive integer as the upper limit
  - Choose counting algorithm
  - Display list of found primes
  - Measure execution time
  - Comprehensive help and examples

- **Complete Test Suite**:
  - 31+ test cases covering all functions
  - Tests for edge cases (0, 1, 2, negative numbers)
  - Consistency checks between algorithms
  - Utility function validation

## Project Structure

```
.
├── src/
│   ├── prime_counter.py    # Core prime counting functions
│   ├── utils.py            # Input validation and output formatting
│   └── main.py             # CLI entry point
├── tests/
│   ├── test_prime_counter.py  # Tests for prime counting
│   └── test_utils.py          # Tests for utilities
└── README.md               # This file
```

## Installation

No external dependencies required - uses only Python standard library (3.7+).

```bash
git clone <repository>
cd <repository>
```

## Usage

### Basic Usage

Count primes before a number (default: using sieve algorithm):

```bash
python src/main.py 100
```

Output:
```
Found 25 prime numbers before 100
```

### Show List of Primes

Display the actual primes found:

```bash
python src/main.py 100 --show-primes
```

Output:
```
Found 25 prime numbers before 100
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

### Measure Execution Time

Compare performance of algorithms:

```bash
# Sieve method (faster for large ranges)
python src/main.py 10000 --method sieve --time

# Basic method
python src/main.py 10000 --method basic --time
```

### Choose Algorithm

```bash
# Using sieve (default, faster)
python src/main.py 1000 --method sieve

# Using basic iteration
python src/main.py 1000 --method basic
```

### Get Help

```bash
python src/main.py --help
```

## Implementation Steps

This implementation includes the following key components:

### 1. Core Prime Checking (`src/prime_counter.py`)
- **`is_prime(n)`**: Determines if a single number is prime using trial division up to √n
- **`count_primes_before(n)`**: Counts all primes before n using basic iteration
- **`sieve_of_eratosthenes(n)`**: Counts primes using the efficient Sieve algorithm
- **`get_primes_before(n)`**: Returns list of all primes before n

### 2. Input Validation & Output Formatting (`src/utils.py`)
- **`validate_input(value)`**: Ensures input is a valid non-negative integer
- **`format_output(...)`**: Formats results with optional prime lists and timing info

### 3. Command-Line Interface (`src/main.py`)
- Argument parsing with argparse
- Supports multiple algorithms
- Optional display of primes and timing
- Error handling with user-friendly messages

### 4. Comprehensive Testing (`tests/`)
- **31 tests for prime counting**: Edge cases, small/large numbers, consistency checks
- **12 tests for utilities**: Input validation, output formatting
- All tests passing

## Algorithm Complexity

### Basic Iteration (`count_primes_before`)
- **Time Complexity**: O(n × √n)
- **Space Complexity**: O(1)
- Best for: Small ranges (n < 10,000)

### Sieve of Eratosthenes (`sieve_of_eratosthenes`)
- **Time Complexity**: O(n log log n)
- **Space Complexity**: O(n)
- Best for: Large ranges (n ≥ 10,000)

## Examples

### Example 1: Count primes before 20
```bash
$ python src/main.py 20
Found 8 prime numbers before 20
```
Primes: 2, 3, 5, 7, 11, 13, 17, 19

### Example 2: Find all primes before 30
```bash
$ python src/main.py 30 --show-primes
Found 10 prime numbers before 30
Primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Example 3: Performance comparison
```bash
$ python src/main.py 100000 --method sieve --time
Found 9592 prime numbers before 100000
Execution time: 0.012345 seconds

$ python src/main.py 100000 --method basic --time
Found 9592 prime numbers before 100000
Execution time: 0.456789 seconds
```

## Testing

Run all tests:

```bash
cd tests
python -m pytest . -v
# or
python -m unittest discover -v
```

Run specific test file:

```bash
python -m pytest test_prime_counter.py -v
python -m pytest test_utils.py -v
```

## Key Test Cases

- **Edge Cases**: 0, 1, 2, negative numbers
- **Small Ranges**: 3, 10, 20 (known results)
- **Medium Ranges**: 100, 1000 (25, 168 primes respectively)
- **Algorithm Consistency**: Verify sieve matches basic iteration
- **Correctness**: All 25 primes before 100 verified
- **Input Validation**: Invalid inputs, empty strings, non-integers

## Performance Notes

- The sieve algorithm is significantly faster for ranges > 10,000
- For very large numbers (> 1,000,000), both methods take longer but sieve remains more efficient
- Memory usage becomes a consideration only for extremely large ranges (> 10,000,000)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
