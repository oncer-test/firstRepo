# firstRepo - Quick Sort Algorithm Implementation

A comprehensive implementation of the Quick Sort algorithm in Python with extensive documentation and examples.

## Overview

This repository contains a production-quality implementation of the Quick Sort sorting algorithm with:
- Detailed module-level documentation explaining the algorithm
- Comprehensive docstrings for all functions
- Inline code comments explaining the logic
- Type hints for better code clarity
- Multiple implementations (simple recursive and in-place)
- Extensive test cases demonstrating various scenarios

## Files

### `quicksort.py`
The main implementation file containing:
- **`quicksort(arr)`** - Simple recursive implementation that returns a new sorted list
- **`quicksort_inplace(arr, low, high)`** - Optimized in-place implementation
- **`partition(arr, low, high)`** - Helper function using Lomuto partition scheme

## Algorithm Details

### What is Quick Sort?
Quick Sort is a divide-and-conquer algorithm that efficiently sorts arrays by:
1. Selecting a pivot element
2. Partitioning the array around the pivot
3. Recursively sorting the resulting subarrays

### Complexity Analysis

| Aspect | Complexity |
|--------|-----------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |
| Space (Simple) | O(n) |
| Space (In-place) | O(log n) average |

### When to Use
- When you need efficient average-case O(n log n) performance
- When in-place sorting with minimal extra space is important
- For large datasets where cache efficiency matters
- As a general-purpose sorting solution

## Usage

### Simple Recursive Implementation
```python
from quicksort import quicksort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### In-Place Implementation
```python
from quicksort import quicksort_inplace

arr = [64, 34, 25, 12, 22, 11, 90]
quicksort_inplace(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### Supported Data Types
The implementation works with any comparable data types:
- Integers: `quicksort([5, 2, 8, 1])`
- Floats: `quicksort([3.14, 2.71, 1.41])`
- Strings: `quicksort(['banana', 'apple', 'cherry'])`
- Custom objects: Any class implementing comparison operators

## Running the Examples

Execute the demonstration script:
```bash
python quicksort.py
```

This will run 8 test cases covering:
1. Random unsorted arrays
2. Already sorted arrays
3. Reverse sorted arrays
4. Arrays with duplicates
5. Single element arrays
6. Empty arrays
7. In-place sorting
8. Sorting strings

## Key Features

### Comprehensive Documentation
- **Module-level docstring**: Algorithm overview, complexity analysis, and use cases
- **Function docstrings**: Detailed parameter descriptions, return values, and examples
- **Inline comments**: Explanation of algorithm logic and implementation details

### Code Quality
- **Type hints**: Full type annotations for better IDE support and clarity
- **Pythonic code**: Follows PEP 8 style guidelines
- **Readable implementation**: Clear variable names and logical structure

### Multiple Implementations
- **Simple recursive**: Easy to understand, creates new lists
- **In-place**: Memory-efficient version for large datasets
- **Partition helper**: Reusable partition function

## Algorithm Explanation

### Partition Scheme (Lomuto)
The implementation uses the Lomuto partition scheme:
1. Select the last element as the pivot
2. Maintain an index to track the boundary of smaller elements
3. Traverse and compare each element with the pivot
4. Swap elements to place smaller elements on the left
5. Place pivot in its final sorted position

### Recursive Process
1. Base case: Arrays with ≤1 element are already sorted
2. Partition the array around a pivot
3. Recursively sort the left partition (elements < pivot)
4. Recursively sort the right partition (elements > pivot)
5. Combine the results

## References

- C.A.R. Hoare, "Quicksort", The Computer Journal, 1962
- Cormen, Leiserson, Rivest, Stein - Introduction to Algorithms (CLRS)
- Wikipedia: https://en.wikipedia.org/wiki/Quicksort

## License

MIT License - See LICENSE file for details

## Author

Created as an educational implementation of the Quick Sort algorithm.
