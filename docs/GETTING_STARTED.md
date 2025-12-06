# Getting Started Guide

Welcome! This guide will help you set up and run the different Fibonacci implementations in this repository.

## Repository Overview

This repository contains implementations across multiple branches. Each branch has its own implementation with different characteristics.

## Quick Navigation

### Want JavaScript?
- **Branch:** `origin/agent/06474ca6-4286-472d-85bc-218fadf107ad-make-exponential-fibonac`
- **Type:** Exponential Fibonacci
- **Features:** Iterative, sequence generation, memoized
- **Tests:** 12 comprehensive test cases
- **Go to:** [JavaScript Setup](#javascript-exponential-fibonacci-setup)

### Want Python?
- **Enhanced:** `origin/agent/b630c2fb-40e9-46a3-8153-9aeb150e4ed1-make-a-fibonnaci-sequenc` (with multiplier support)
- **Original:** `origin/agent/a90b4c0d-6dfa-496f-ab80-6c3f6012ba6b-create-a-python-script-f` (basic implementation)
- **Go to:** [Python Setup](#python-setup)

## JavaScript (Exponential Fibonacci) Setup

### Prerequisites
- Node.js (v16 or higher)
- npm (usually comes with Node.js)

### Installation

```bash
# Checkout the JavaScript implementation branch
git checkout origin/agent/06474ca6-4286-472d-85bc-218fadf107ad-make-exponential-fibonac

# Install dependencies
npm install
```

### Running Tests

```bash
# Run the full test suite
npm test
```

Expected output: All 12 tests pass, covering:
- Basic values (small n)
- Larger values
- Invalid input handling
- Sequence generation
- Memoization functionality
- Cross-method consistency

### Usage Examples

```javascript
import { exponentialFibonacci } from './src/index.js';

// Single value computation
console.log(exponentialFibonacci(5));   // 11
console.log(exponentialFibonacci(10));  // 683

// Sequence generation
import { exponentialFibonacciSequence } from './src/index.js';
const seq = exponentialFibonacciSequence(5);
console.log(seq);  // [0, 1, 1, 3, 5, 11, 21]

// Memoized version for repeated calls
import { createMemoizedFibonacci } from './src/index.js';
const fib = createMemoizedFibonacci();
console.log(fib(5));   // 11 (computed)
console.log(fib(5));   // 11 (cached)
```

### Documentation

- **API Reference:** `docs/API.md` - Detailed function documentation
- **Algorithm Guide:** `docs/ALGORITHM.md` - Mathematical analysis and properties

## Python Setup

### Prerequisites
- Python 3.6 or higher

### Installation

```bash
# For Enhanced Version (with multiplier support)
git checkout origin/agent/b630c2fb-40e9-46a3-8153-9aeb150e4ed1-make-a-fibonnaci-sequenc

# For Original Version
git checkout origin/agent/a90b4c0d-6dfa-496f-ab80-6c3f6012ba6b-create-a-python-script-f

# No additional installation required
```

### Basic Usage

```bash
# Compute 10th Fibonacci number
python fib.py 10

# Using iterative method (default)
python fib.py --method iterative 5

# Using memoized method
python fib.py --method memoized 15

# With multiplier (enhanced version only)
python fib.py --multiply 2 10
```

### Python Code Examples

```python
from fib import fib_iterative, fib_memoized

# Iterative approach
result = fib_iterative(10)
print(result)  # 55

# Memoized approach (recursive with caching)
result = fib_memoized(15)
print(result)  # 610

# With multiplier (enhanced version)
from fib import fib_multiplied_iterative
result = fib_multiplied_iterative(10, 2)
print(result)  # 110 (55 * 2)
```

### Testing

The Python implementations use docstring examples (doctest format). To run:

```bash
python -m doctest fib.py -v
```

## Choosing the Right Implementation

| Aspect | JavaScript | Python Enhanced | Python Original |
|--------|-----------|-----------------|-----------------|
| Algorithm | Exponential Fibonacci | Standard Fibonacci | Standard Fibonacci |
| Implementations | 3 | 4 | 2 |
| Multiplier Support | No | Yes | No |
| CLI Interface | No | Yes | Yes |
| Test Framework | Node.js native test | Doctest | Doctest |
| Documentation | Excellent | Good | Good |
| Use Case | Learning, algorithms | General purpose | Simplicity |

## Common Issues

### JavaScript

**Issue:** `Error: Cannot find module`
- **Solution:** Make sure you ran `npm install` first

**Issue:** Tests not running
- **Solution:** Ensure Node.js version is 16+. Check with `node --version`

### Python

**Issue:** `ModuleNotFoundError` when importing
- **Solution:** Make sure you're in the correct branch with the fib.py file

**Issue:** CLI arguments not recognized
- **Solution:** Check you're using the correct branch. Enhanced version has multiplier support, original doesn't.

## Next Steps

1. **Read the Implementation Comparison:** [IMPLEMENTATION_COMPARISON.md](IMPLEMENTATION_COMPARISON.md)
2. **Understand the Architecture:** [ARCHITECTURE.md](ARCHITECTURE.md)
3. **Review Branch-specific Docs:** Each branch has its own README with detailed examples
4. **Contribute:** See [CONTRIBUTING.md](CONTRIBUTING.md)

## Additional Resources

- **Main README:** [README.md](../README.md)
- **Branch Documentation:** Each branch contains a README.md with language-specific details
- **Source Code:** Inline JSDoc (JS) and docstrings (Python) provide function-level documentation
