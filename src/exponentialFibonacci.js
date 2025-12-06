/**
 * Computes the nth exponential fibonacci number.
 *
 * The exponential fibonacci sequence is defined as:
 * E(0) = 0
 * E(1) = 1
 * E(n) = E(n-1) + 2 * E(n-2) for n > 1
 *
 * This produces the sequence: 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, ...
 *
 * @param {number} n - The position in the sequence (must be a non-negative integer)
 * @returns {number} The nth exponential fibonacci number
 * @throws {Error} If n is negative
 */
export function exponentialFibonacci(n) {
  if (!Number.isInteger(n) || n < 0) {
    throw new Error('Input must be a non-negative integer');
  }

  if (n === 0) return 0;
  if (n === 1) return 1;

  let prev2 = 0;
  let prev1 = 1;

  for (let i = 2; i <= n; i++) {
    const current = prev1 + 2 * prev2;
    prev2 = prev1;
    prev1 = current;
  }

  return prev1;
}

/**
 * Computes multiple exponential fibonacci numbers up to n.
 * Useful for generating sequences.
 *
 * @param {number} n - The upper bound (inclusive)
 * @returns {number[]} Array of exponential fibonacci numbers from E(0) to E(n)
 * @throws {Error} If n is negative
 */
export function exponentialFibonacciSequence(n) {
  if (!Number.isInteger(n) || n < 0) {
    throw new Error('Input must be a non-negative integer');
  }

  const sequence = [];
  let prev2 = 0;
  let prev1 = 1;

  sequence.push(prev2);
  if (n > 0) sequence.push(prev1);

  for (let i = 2; i <= n; i++) {
    const current = prev1 + 2 * prev2;
    sequence.push(current);
    prev2 = prev1;
    prev1 = current;
  }

  return sequence;
}

/**
 * Memoized version of exponential fibonacci for repeated computations.
 * Stores computed values to avoid recalculation.
 */
export function createMemoizedFibonacci() {
  const cache = {};

  return function memoizedExponentialFibonacci(n) {
    if (!Number.isInteger(n) || n < 0) {
      throw new Error('Input must be a non-negative integer');
    }

    if (n in cache) return cache[n];

    let result;
    if (n === 0) {
      result = 0;
    } else if (n === 1) {
      result = 1;
    } else {
      result = memoizedExponentialFibonacci(n - 1) + 2 * memoizedExponentialFibonacci(n - 2);
    }

    cache[n] = result;
    return result;
  };
}
