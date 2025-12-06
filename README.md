# firstRepo

A Python module for computing Fibonacci numbers with optional multiplication support.

## Overview

This repository provides efficient implementations of Fibonacci number computation with two main features:

1. **Multiple Computation Methods**: Iterative and memoized approaches with different performance characteristics
2. **Multiplied Sequences**: Multiply Fibonacci numbers by a given factor for scaled sequences

## Features

### Standard Fibonacci
- **Iterative Method**: Memory-efficient O(1) space complexity
- **Memoized Method**: Optimized for repeated calculations with O(n) space

### Multiplied Fibonacci
- **Multiplied Iterative**: Standard Fibonacci multiplied by a factor using iterative method
- **Multiplied Memoized**: Standard Fibonacci multiplied by a factor using memoization

## Installation & Requirements

- Python 3.6+
- No external dependencies required

## Complexity Analysis

### Standard Fibonacci

| Method | Time | Space | Best For |
|--------|------|-------|----------|
| Iterative | O(n) | O(1) | Memory-constrained environments |
| Memoized | O(n) | O(n) | Repeated calculations |

### Multiplied Fibonacci

The multiplied variants maintain the same complexity characteristics as their base implementations:
- **Iterative**: O(n) time, O(1) space
- **Memoized**: O(n) time, O(n) space

## Usage

### Command Line Interface

Basic usage:
```bash
python fib.py 10
# Output: fib(10) = 55
```

Specify method:
```bash
python fib.py --method iterative 10
# Output: fib(10) = 55

python fib.py --method memoized 10
# Output: fib(10) = 55
```

Multiply Fibonacci results:
```bash
python fib.py --multiply 2 10
# Output: fib(10) * 2 = 110

python fib.py --method memoized --multiply 3 15
# Output: fib(15) * 3 = 1215
```

Multiple values:
```bash
python fib.py --method memoized --multiply 2 5 10 15
# Output:
# fib(5) * 2 = 10
# fib(10) * 2 = 110
# fib(15) * 2 = 610
```

### Programmatic Usage

```python
from fib import fib_iterative, fib_memoized, fib_multiplied_iterative, fib_multiplied_memoized

# Standard Fibonacci
result = fib_iterative(10)          # Returns 55
result = fib_memoized(10)           # Returns 55

# Multiplied Fibonacci
result = fib_multiplied_iterative(10, 2)   # Returns 110
result = fib_multiplied_memoized(10, 3)    # Returns 165
```

## Examples

### Example 1: Standard Fibonacci Sequence
```bash
python fib.py 0
# Output: fib(0) = 0

python fib.py 5
# Output: fib(5) = 5

python fib.py 20
# Output: fib(20) = 6765
```

### Example 2: Fibonacci Multiplied by 2
```bash
python fib.py --multiply 2 5
# Output: fib(5) * 2 = 10

python fib.py --multiply 2 20
# Output: fib(20) * 2 = 13530
```

### Example 3: Fibonacci Multiplied by 3 (Memoized)
```bash
python fib.py --method memoized --multiply 3 15
# Output: fib(15) * 3 = 1215
```

### Example 4: Multiple Calculations with Scaling
```bash
python fib.py --multiply 5 10 15 20
# Output:
# fib(10) * 5 = 275
# fib(15) * 5 = 1525
# fib(20) * 5 = 33825
```

## Edge Cases

### Multiplier = 1
When multiplier is 1, the result equals the standard Fibonacci number:
```bash
python fib.py --multiply 1 10
# Output: fib(10) * 1 = 55
```

### Zero Position
Fibonacci(0) is always 0, regardless of multiplier:
```bash
python fib.py --multiply 2 0
# Output: fib(0) * 2 = 0
```

### Large Multipliers
Multipliers can be any positive integer:
```bash
python fib.py --multiply 100 10
# Output: fib(10) * 100 = 5500
```

### Invalid Inputs
The module validates inputs and provides clear error messages:
```bash
python fib.py --multiply 0 10
# Error: multiplier must be positive

python fib.py -5
# Error: n must be non-negative
```

## Algorithm Details

### Iterative Method
The iterative approach uses a simple two-variable window to track consecutive Fibonacci numbers:
- Maintains only the previous and current values
- Single pass through the sequence
- Ideal for single calculations with memory constraints

### Memoized Method
The memoized approach uses recursion with caching:
- Stores computed values in a dictionary
- Fast for repeated calculations of different values
- Better for scenarios where you compute many Fibonacci numbers

### Multiplication
Both multiplied variants:
- First compute the standard Fibonacci number
- Then multiply the result by the provided factor
- No additional complexity added by multiplication

## Implementation Details

All functions include:
- **Type hints**: Full type annotations for clarity
- **Docstrings**: Google-style documentation with examples
- **Error handling**: Validation with descriptive error messages
- **CLI integration**: Convenient command-line interface

## Running Instructions

1. Ensure Python 3.6+ is installed
2. Run directly:
   ```bash
   python fib.py [options] <n>
   ```
3. For help:
   ```bash
   python fib.py
   ```

## Performance Notes

- **For single calculations**: Use iterative method for better memory efficiency
- **For repeated calculations**: Use memoized method to avoid recomputation
- **For scaled sequences**: Multiplied variants maintain the same efficiency as base methods
- **For large n values**: Both methods scale linearly with O(n) time complexity
