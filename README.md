# Exponential Fibonacci Library

A high-performance JavaScript library for computing exponential fibonacci numbers efficiently.

## Overview

The exponential fibonacci sequence grows exponentially with the recurrence relation:

```
E(n) = E(n-1) + 2 × E(n-2)
```

This produces the sequence: **0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, ...**

## Quick Start

### Installation

```bash
npm install
```

### Basic Usage

```javascript
import { exponentialFibonacci } from './src/index.js';

// Compute a single value
console.log(exponentialFibonacci(5));    // 11
console.log(exponentialFibonacci(10));   // 683
console.log(exponentialFibonacci(20));   // 699,050
```

## API Reference

### `exponentialFibonacci(n)`

Computes the nth exponential fibonacci number.

- **Parameters:** n (non-negative integer)
- **Returns:** The nth exponential fibonacci number
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

```javascript
import { exponentialFibonacci } from './src/index.js';

exponentialFibonacci(0);   // 0
exponentialFibonacci(5);   // 11
exponentialFibonacci(10);  // 683
```

### `exponentialFibonacciSequence(n)`

Generates all exponential fibonacci numbers from 0 to n.

- **Parameters:** n (non-negative integer)
- **Returns:** Array of exponential fibonacci numbers
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

```javascript
import { exponentialFibonacciSequence } from './src/index.js';

exponentialFibonacciSequence(5);
// [0, 1, 1, 3, 5, 11, 21]
```

### `createMemoizedFibonacci()`

Creates a memoized fibonacci function for efficient repeated computations.

- **Returns:** Memoized exponential fibonacci function
- **Time Complexity:** O(n) first call, O(1) for cached values
- **Space Complexity:** O(n)

```javascript
import { createMemoizedFibonacci } from './src/index.js';

const fib = createMemoizedFibonacci();
console.log(fib(5));   // 11 (computed)
console.log(fib(5));   // 11 (cached)
console.log(fib(10));  // 683 (computed)
```

## Documentation

- **[API Documentation](docs/API.md)** - Detailed function signatures and examples
- **[Algorithm Guide](docs/ALGORITHM.md)** - Mathematical properties, complexity analysis, and implementation approaches

## Examples

### Example 1: Generate Sequence

```javascript
import { exponentialFibonacciSequence } from './src/index.js';

const sequence = exponentialFibonacciSequence(10);
console.log(sequence);
// [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683]
```

### Example 2: Using Memoized Version

```javascript
import { createMemoizedFibonacci } from './src/index.js';

const fib = createMemoizedFibonacci();
const values = [5, 10, 15, 10, 5];  // Note: 10 and 5 are repeated

for (const n of values) {
  console.log(`E(${n}) = ${fib(n)}`);
}
// Cached lookups are instant for repeated values
```

### Example 3: Large Values

```javascript
import { exponentialFibonacci } from './src/index.js';

// Exponential fibonacci grows very fast
console.log(exponentialFibonacci(25));   // 22,369,621
console.log(exponentialFibonacci(30));   // 357,913,941
```

## Performance

The iterative approach is recommended for general use:
- **Time:** O(n) - linear time
- **Space:** O(1) - constant memory

For repeated computations, use the memoized version to cache results.

## Testing

Run the test suite:

```bash
npm test
```

## Algorithm Details

The exponential fibonacci sequence has interesting mathematical properties:

1. **Growth Rate:** E(n) ~ 2ⁿ / 3 (exponential)
2. **Closed Form:** E(n) = (2ⁿ - (-1)ⁿ) / 3
3. **Characteristic Roots:** 2 and -1

For detailed algorithmic analysis, see [Algorithm Guide](docs/ALGORITHM.md).

## License

MIT - See [LICENSE](LICENSE) file for details
