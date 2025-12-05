# firstRepo

This is first repo

## Fibonacci Numbers Script

A Python script that computes Fibonacci numbers using two different algorithms: iterative and memoized approaches. Choose the method based on your performance and memory requirements.

### Overview

The `fib.py` script provides efficient implementations for computing the nth Fibonacci number with different time/space trade-offs:

- **Iterative Method**: Best for single computations or memory-constrained environments
- **Memoized Method**: Best for multiple calls or when caching results is beneficial

### Usage

#### Basic Usage (Iterative - Default)

```bash
python fib.py 10
# Output: fib(10) = 55
```

#### Iterative Method (Explicit)

```bash
python fib.py --method iterative 10
# Output: fib(10) = 55
```

#### Memoized Method

```bash
python fib.py --method memoized 10
# Output: fib(10) = 55
```

#### Computing Multiple Values

```bash
python fib.py --method iterative 5 10 15
# Output:
# fib(5) = 5
# fib(10) = 55
# fib(15) = 610
```

```bash
python fib.py --method memoized 5 10 15 20 25
# Output:
# fib(5) = 5
# fib(10) = 55
# fib(15) = 610
# fib(20) = 6765
# fib(25) = 75025
```

### Complexity Analysis

#### Iterative Method

```
Time Complexity:  O(n)
Space Complexity: O(1)
```

**Characteristics:**
- Uses a simple loop with constant space
- Computes the result by maintaining only two variables (previous and current)
- No recursion overhead
- Best when you need to compute a single value or want minimal memory usage

**When to use:**
- Computing a single or small number of Fibonacci values
- Memory-constrained environments
- When you don't need to cache results for repeated calls

#### Memoized Method

```
Time Complexity:  O(n)
Space Complexity: O(n)
```

**Characteristics:**
- Uses recursion with memoization to cache computed values
- More readable recursive structure
- Stores all intermediate results in a dictionary
- Subsequent calls to cached values are O(1)

**When to use:**
- Computing multiple different Fibonacci numbers
- When you benefit from caching previously computed results
- Applications where readability is important
- When the additional O(n) space is acceptable

### Algorithm Comparison

| Aspect | Iterative | Memoized |
|--------|-----------|----------|
| Time Complexity | O(n) | O(n) |
| Space Complexity | O(1) | O(n) |
| Readability | Medium | High |
| Memory Usage | Minimal | Linear |
| Recursion | No | Yes |
| Best For | Single values | Multiple calls |

### Examples

#### Example 1: Computing a Single Fibonacci Number

```bash
$ python fib.py 7
fib(7) = 13

$ python fib.py --method memoized 7
fib(7) = 13
```

**Sequence:** 0, 1, 1, 2, 3, 5, 8, 13...
(The 7th position contains 13)

#### Example 2: Computing Multiple Values with Different Methods

```bash
$ python fib.py --method iterative 0 1 2 3 4 5
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
```

#### Example 3: Larger Numbers

```bash
$ python fib.py --method memoized 30 40 50
fib(30) = 832040
fib(40) = 102334155
fib(50) = 12586269025
```

### Edge Cases

- `fib(0)` returns `0` (base case)
- `fib(1)` returns `1` (base case)
- Negative indices raise a `ValueError`

### Implementation Details

#### Iterative Approach

```python
def fib_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

The iterative method maintains two variables: `prev` (F(n-2)) and `curr` (F(n-1)). In each iteration, we compute the next value and shift the window forward.

#### Memoized Approach

```python
def fib_memoized(n: int, memo: Dict[int, int] = None) -> int:
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
```

The memoized method uses recursion with a cache dictionary. Before computing a value, it checks if it's already cached. This prevents redundant calculations and provides O(1) lookup for previously computed values.

### Performance Notes

- **Iterative:** Ideal for computing single values. No function call overhead.
- **Memoized:** Ideal for computing multiple values in a session. Leverages cached results.
- Both methods complete in O(n) time, but iterative uses constant space vs. linear space for memoized.

### Installation & Requirements

No external dependencies required. Uses only Python 3 standard library:
- `sys` for command-line argument parsing
- `typing` for type hints

Requires Python 3.6+

### Running the Script

Make the script executable:
```bash
chmod +x fib.py
```

Then run directly:
```bash
./fib.py 10
```

Or use python explicitly:
```bash
python fib.py 10
python3 fib.py 10
```
