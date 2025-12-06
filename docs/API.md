# Exponential Fibonacci API Documentation

## Overview

The Exponential Fibonacci library provides efficient functions to compute exponential fibonacci numbers and sequences. The exponential fibonacci sequence grows exponentially, making it useful for mathematical and algorithmic applications.

## Functions

### `exponentialFibonacci(n)`

Computes the nth exponential fibonacci number using an iterative approach.

**Parameters:**
- `n` (number): The position in the sequence (must be a non-negative integer)

**Returns:**
- (number): The nth exponential fibonacci number

**Throws:**
- Error: If n is not a non-negative integer

**Time Complexity:** O(n)
**Space Complexity:** O(1)

**Example:**
```javascript
import { exponentialFibonacci } from './src/index.js';

console.log(exponentialFibonacci(0));   // 0
console.log(exponentialFibonacci(5));   // 11
console.log(exponentialFibonacci(10));  // 683
```

---

### `exponentialFibonacciSequence(n)`

Computes all exponential fibonacci numbers from position 0 to n (inclusive).

**Parameters:**
- `n` (number): The upper bound (inclusive, must be a non-negative integer)

**Returns:**
- (number[]): Array of exponential fibonacci numbers from E(0) to E(n)

**Throws:**
- Error: If n is not a non-negative integer

**Time Complexity:** O(n)
**Space Complexity:** O(n)

**Example:**
```javascript
import { exponentialFibonacciSequence } from './src/index.js';

console.log(exponentialFibonacciSequence(5));
// Output: [0, 1, 1, 3, 5, 11, 21]
```

---

### `createMemoizedFibonacci()`

Creates a memoized exponential fibonacci function for efficient repeated computations. Uses a cache to store previously computed values.

**Returns:**
- (function): A memoized exponential fibonacci function

**Time Complexity:** O(n) for first call, O(1) for cached values
**Space Complexity:** O(n) for cache storage

**Example:**
```javascript
import { createMemoizedFibonacci } from './src/index.js';

const fibonacci = createMemoizedFibonacci();

console.log(fibonacci(5));   // Computed: 11
console.log(fibonacci(5));   // Cached: 11
console.log(fibonacci(10));  // Computed: 683
```

---

## Formula

The exponential fibonacci sequence is defined by the recurrence relation:

```
E(0) = 0
E(1) = 1
E(n) = E(n-1) + 2 * E(n-2)  for n > 1
```

This produces the sequence: **0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, ...**

## Performance Characteristics

| Function | Time | Space | Use Case |
|----------|------|-------|----------|
| `exponentialFibonacci(n)` | O(n) | O(1) | Single value computation |
| `exponentialFibonacciSequence(n)` | O(n) | O(n) | Generating sequences |
| `memoizedFibonacci(n)` | O(n)* | O(n) | Repeated computations |

*First call is O(n), subsequent calls for cached values are O(1)
