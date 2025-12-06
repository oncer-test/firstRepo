import { test } from 'node:test';
import assert from 'node:assert/strict';
import { exponentialFibonacci, exponentialFibonacciSequence, createMemoizedFibonacci } from '../src/index.js';

test('exponentialFibonacci - basic values', () => {
  assert.equal(exponentialFibonacci(0), 0);
  assert.equal(exponentialFibonacci(1), 1);
  assert.equal(exponentialFibonacci(2), 1);
  assert.equal(exponentialFibonacci(3), 3);
  assert.equal(exponentialFibonacci(4), 5);
  assert.equal(exponentialFibonacci(5), 11);
});

test('exponentialFibonacci - larger values', () => {
  assert.equal(exponentialFibonacci(6), 21);
  assert.equal(exponentialFibonacci(7), 43);
  assert.equal(exponentialFibonacci(8), 85);
  assert.equal(exponentialFibonacci(9), 171);
  assert.equal(exponentialFibonacci(10), 341);
});

test('exponentialFibonacci - invalid input', () => {
  assert.throws(() => exponentialFibonacci(-1), /non-negative integer/);
  assert.throws(() => exponentialFibonacci(1.5), /non-negative integer/);
  assert.throws(() => exponentialFibonacci('5'), /non-negative integer/);
  assert.throws(() => exponentialFibonacci(null), /non-negative integer/);
});

test('exponentialFibonacciSequence - basic sequences', () => {
  assert.deepEqual(exponentialFibonacciSequence(0), [0]);
  assert.deepEqual(exponentialFibonacciSequence(1), [0, 1]);
  assert.deepEqual(exponentialFibonacciSequence(2), [0, 1, 1]);
  assert.deepEqual(exponentialFibonacciSequence(5), [0, 1, 1, 3, 5, 11]);
});

test('exponentialFibonacciSequence - longer sequences', () => {
  const seq = exponentialFibonacciSequence(10);
  assert.deepEqual(seq, [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341]);
  assert.equal(seq.length, 11);
});

test('exponentialFibonacciSequence - invalid input', () => {
  assert.throws(() => exponentialFibonacciSequence(-1), /non-negative integer/);
  assert.throws(() => exponentialFibonacciSequence(2.5), /non-negative integer/);
});

test('memoized fibonacci - basic functionality', () => {
  const fib = createMemoizedFibonacci();
  assert.equal(fib(0), 0);
  assert.equal(fib(1), 1);
  assert.equal(fib(5), 11);
  assert.equal(fib(10), 341);
});

test('memoized fibonacci - cached values are consistent', () => {
  const fib = createMemoizedFibonacci();
  const result1 = fib(7);
  const result2 = fib(7);
  assert.equal(result1, result2);
  assert.equal(result1, 43);
});

test('memoized fibonacci - invalid input', () => {
  const fib = createMemoizedFibonacci();
  assert.throws(() => fib(-1), /non-negative integer/);
  assert.throws(() => fib(3.2), /non-negative integer/);
});

test('exponentialFibonacci - consistency across methods', () => {
  const iterValue = exponentialFibonacci(8);
  const seqValue = exponentialFibonacciSequence(8)[8];
  const memoized = createMemoizedFibonacci();
  const memoValue = memoized(8);

  assert.equal(iterValue, seqValue);
  assert.equal(iterValue, memoValue);
  assert.equal(iterValue, 85);
});

test('exponentialFibonacci - very large values', () => {
  assert.equal(exponentialFibonacci(20), 349525);
  assert.equal(exponentialFibonacci(25), 11184811);
});

test('exponentialFibonacci - recurrence relation verification', () => {
  // Verify: E(n) = E(n-1) + 2*E(n-2)
  for (let n = 2; n <= 15; n++) {
    const enMinus1 = exponentialFibonacci(n - 1);
    const enMinus2 = exponentialFibonacci(n - 2);
    const en = exponentialFibonacci(n);
    assert.equal(en, enMinus1 + 2 * enMinus2, `Recurrence failed for n=${n}`);
  }
});
