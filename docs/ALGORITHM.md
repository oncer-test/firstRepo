# Exponential Fibonacci Algorithm Guide

## Definition

The exponential fibonacci sequence is a generalization of the standard Fibonacci sequence with a different recurrence relation:

```
E(0) = 0
E(1) = 1
E(n) = E(n-1) + 2 * E(n-2)  for n ≥ 2
```

The coefficient 2 applied to E(n-2) causes the sequence to grow exponentially, hence the name.

## Sequence Values

| n | E(n) | Growth Factor |
|---|------|---------------|
| 0 | 0 | - |
| 1 | 1 | - |
| 2 | 1 | 1.0x |
| 3 | 3 | 3.0x |
| 4 | 5 | 1.67x |
| 5 | 11 | 2.2x |
| 6 | 21 | 1.91x |
| 7 | 43 | 2.05x |
| 8 | 85 | 1.98x |
| 9 | 171 | 2.01x |
| 10 | 341 | 1.99x |

## Mathematical Properties

### Closed Form (Characteristic Equation Method)

Using the characteristic equation method for linear recurrences:

The characteristic equation is: `x² - x - 2 = 0`

This factors as: `(x - 2)(x + 1) = 0`

Roots: `r₁ = 2` and `r₂ = -1`

Therefore, the closed form is:

```
E(n) = A × 2ⁿ + B × (-1)ⁿ
```

Using boundary conditions E(0) = 0 and E(1) = 1:
- `A + B = 0`
- `2A - B = 1`

Solving: `A = 1/3` and `B = -1/3`

**Closed Form:**
```
E(n) = (2ⁿ - (-1)ⁿ) / 3
```

### Growth Rate

The dominant term is `2ⁿ / 3`, so:

- **Asymptotic Growth:** E(n) ~ 2ⁿ / 3
- **Growth Pattern:** Exponential with base 2
- **Doubling Point:** Approximately every 3-4 values

## Implementation Approaches

### 1. Iterative (Recommended for Single Values)

**Advantages:**
- Linear time complexity O(n)
- Constant space O(1)
- No recursion overhead
- Safe from stack overflow

**Disadvantages:**
- Cannot reuse subproblem solutions across function calls

**Use When:** Computing single values or small sequences

### 2. Dynamic Programming with Memoization

**Advantages:**
- O(n) time for first computation
- O(1) lookup for repeated values
- Recursive structure follows the definition

**Disadvantages:**
- Higher space complexity O(n)
- Recursive call overhead

**Use When:** Computing multiple different values repeatedly

### 3. Closed Form (Direct Calculation)

**Advantages:**
- O(1) time (with fast exponentiation)
- O(1) space

**Disadvantages:**
- Floating point precision issues for large n
- Requires arbitrary precision arithmetic for exact results

**Use When:** Extremely large n values where precision isn't critical

## Complexity Analysis

### Time Complexity

| Approach | Complexity | Notes |
|----------|-----------|-------|
| Iterative | O(n) | Single pass through loop |
| Memoized (first call) | O(n) | Recursive with caching |
| Memoized (cached) | O(1) | Lookup in cache |
| Sequence generation | O(n) | Must compute all values up to n |

### Space Complexity

| Approach | Complexity | Notes |
|----------|-----------|-------|
| Iterative | O(1) | Only stores two variables |
| Memoized | O(n) | Cache stores up to n values |
| Sequence | O(n) | Output array of size n |

## Algorithm Walkthrough: Computing E(5)

**Iterative Approach:**

```
Initial: prev2 = 0, prev1 = 1

i=2: current = 1 + 2*0 = 1    → prev2 = 1, prev1 = 1
i=3: current = 1 + 2*1 = 3    → prev2 = 1, prev1 = 3
i=4: current = 3 + 2*1 = 5    → prev2 = 3, prev1 = 5
i=5: current = 5 + 2*3 = 11   → prev2 = 5, prev1 = 11

Result: E(5) = 11
```

## Comparison with Standard Fibonacci

**Standard Fibonacci:** F(n) = F(n-1) + F(n-2)
- Growth rate: ~φⁿ where φ ≈ 1.618 (Golden Ratio)
- F(30) ≈ 832,040

**Exponential Fibonacci:** E(n) = E(n-1) + 2×E(n-2)
- Growth rate: ~2ⁿ
- E(30) ≈ 357,913,941

The exponential fibonacci grows much faster due to the coefficient 2 amplifying the previous term's contribution.

## Use Cases

1. **Algorithm Analysis:** Analyzing branching algorithms where each node has 2 children
2. **Combinatorics:** Counting structures with weighted recursive properties
3. **Data Structure Growth:** Modeling exponential growth patterns in trees
4. **Mathematical Sequences:** Pure mathematical interest and number theory
