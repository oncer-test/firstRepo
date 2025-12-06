"""
Quick Sort Algorithm Implementation

This module provides a comprehensive implementation of the Quick Sort algorithm,
one of the most efficient and widely-used sorting algorithms in computer science.

Quick Sort Algorithm Overview:
------------------------------
Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot'
element and partitioning the array around it, then recursively sorting the
resulting subarrays. It's called 'quick' because it's highly efficient in practice,
even though its worst-case time complexity is O(n²).

Key Characteristics:
- Divide-and-Conquer approach: Breaks problem into smaller subproblems
- In-place sorting: Uses minimal extra space (O(log n) for recursion stack)
- Unstable sort: Relative order of equal elements may not be preserved
- Cache-friendly: Good locality of reference due to sequential access patterns

Time Complexity Analysis:
- Best Case: O(n log n) - when pivot divides array evenly
- Average Case: O(n log n) - typical performance with random pivots
- Worst Case: O(n²) - when pivot is always smallest or largest (rare with good pivot selection)

Space Complexity:
- O(log n) - recursion call stack depth in average case
- O(n) - recursion call stack depth in worst case (unbalanced partitions)

When to Use Quick Sort:
- When average O(n log n) performance is acceptable
- When in-place sorting is preferred
- For large datasets where cache efficiency matters
- When you need a practical, efficient sorting solution

References:
- C.A.R. Hoare, "Quicksort", The Computer Journal, 1962
- CLRS Introduction to Algorithms, Chapter 7
"""

from typing import List, Any


def quicksort(arr: List[Any]) -> List[Any]:
    """
    Sorts a list using the Quick Sort algorithm.

    This is a wrapper function that initiates the recursive quicksort process
    on the entire array. It returns a sorted copy of the input list.

    Args:
        arr (List[Any]): A list of comparable elements to be sorted.

    Returns:
        List[Any]: A new sorted list containing all elements from the input.

    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(n) for creating new list + O(log n) for recursion stack

    Examples:
        >>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> quicksort([])
        []

        >>> quicksort([42])
        [42]

        >>> quicksort(['banana', 'apple', 'cherry'])
        ['apple', 'banana', 'cherry']
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Recursive case: partition and sort
    pivot = arr[0]  # Choose first element as pivot

    # Partition into three groups: less than, equal to, greater than pivot
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # Recursively sort and combine: sorted(less) + equal + sorted(greater)
    return quicksort(less) + equal + quicksort(greater)


def quicksort_inplace(arr: List[Any], low: int = 0, high: int = None) -> None:
    """
    Sorts a list in-place using the Quick Sort algorithm.

    This is an optimized version that modifies the input list directly,
    using minimal extra space. Uses the Lomuto partition scheme.

    Args:
        arr (List[Any]): A list of comparable elements to be sorted.
        low (int): Starting index of the subarray (default: 0).
        high (int): Ending index of the subarray (default: len(arr) - 1).

    Returns:
        None: The list is sorted in-place.

    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) average for recursion stack, O(n) worst case

    Examples:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> quicksort_inplace(arr)
        >>> arr
        [1, 1, 2, 3, 4, 5, 6, 9]

        >>> arr = []
        >>> quicksort_inplace(arr)
        >>> arr
        []

        >>> arr = [5, 2, 8, 1, 9]
        >>> quicksort_inplace(arr)
        >>> arr
        [1, 2, 5, 8, 9]
    """
    # Initialize high to last index if not provided
    if high is None:
        high = len(arr) - 1

    # Base case: single element or empty subarray is already sorted
    if low < high:
        # Partition the array and get the pivot position
        pi = partition(arr, low, high)

        # Recursively sort the left partition (elements less than pivot)
        quicksort_inplace(arr, low, pi - 1)

        # Recursively sort the right partition (elements greater than pivot)
        quicksort_inplace(arr, pi + 1, high)


def partition(arr: List[Any], low: int, high: int) -> int:
    """
    Partitions an array around a pivot element using the Lomuto scheme.

    This helper function divides the subarray arr[low:high+1] into two parts:
    - Left part: all elements <= pivot
    - Right part: all elements > pivot

    The Lomuto partition scheme uses the last element as the pivot and maintains
    an index to track the boundary between partitions.

    Args:
        arr (List[Any]): The list to partition.
        low (int): Starting index of the subarray.
        high (int): Ending index of the subarray.

    Returns:
        int: The final position of the pivot element.

    Time Complexity: O(n) where n = high - low + 1
    Space Complexity: O(1) - only uses constant extra space

    Algorithm Steps:
    1. Choose the element at index 'high' as the pivot
    2. Maintain an index 'i' to track the boundary of smaller elements
    3. Compare each element with the pivot:
       - If element <= pivot: swap with arr[i] and increment i
       - If element > pivot: continue
    4. Place pivot in its final sorted position by swapping arr[i] and arr[high]
    5. Return i as the pivot's final position

    Example:
        >>> arr = [10, 7, 8, 9, 1, 5]
        >>> pi = partition(arr, 0, 5)
        >>> pi  # pivot position (value at arr[pi] is the pivot)
        4
    """
    # Choose the last element as the pivot
    pivot = arr[high]

    # Index to track the boundary between smaller and larger elements
    # All elements from low to i-1 will be <= pivot
    i = low - 1

    # Traverse through all elements, comparing with the pivot
    for j in range(low, high):
        # If current element is less than or equal to pivot,
        # swap it with the element at position i+1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its final sorted position
    # All elements before this position are <= pivot
    # All elements after this position are > pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the final position of the pivot
    return i + 1


if __name__ == "__main__":
    """
    Demonstration and testing of Quick Sort implementations.
    """
    print("=" * 60)
    print("Quick Sort Algorithm Demonstration")
    print("=" * 60)

    # Test case 1: Random unsorted array
    print("\n1. Random unsorted array:")
    test_array_1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"   Original: {test_array_1}")
    sorted_array_1 = quicksort(test_array_1)
    print(f"   Sorted:   {sorted_array_1}")

    # Test case 2: Already sorted array
    print("\n2. Already sorted array:")
    test_array_2 = [1, 2, 3, 4, 5]
    print(f"   Original: {test_array_2}")
    sorted_array_2 = quicksort(test_array_2)
    print(f"   Sorted:   {sorted_array_2}")

    # Test case 3: Reverse sorted array
    print("\n3. Reverse sorted array:")
    test_array_3 = [5, 4, 3, 2, 1]
    print(f"   Original: {test_array_3}")
    sorted_array_3 = quicksort(test_array_3)
    print(f"   Sorted:   {sorted_array_3}")

    # Test case 4: Array with duplicates
    print("\n4. Array with duplicate elements:")
    test_array_4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"   Original: {test_array_4}")
    sorted_array_4 = quicksort(test_array_4)
    print(f"   Sorted:   {sorted_array_4}")

    # Test case 5: Single element
    print("\n5. Single element array:")
    test_array_5 = [42]
    print(f"   Original: {test_array_5}")
    sorted_array_5 = quicksort(test_array_5)
    print(f"   Sorted:   {sorted_array_5}")

    # Test case 6: Empty array
    print("\n6. Empty array:")
    test_array_6 = []
    print(f"   Original: {test_array_6}")
    sorted_array_6 = quicksort(test_array_6)
    print(f"   Sorted:   {sorted_array_6}")

    # Test case 7: In-place sorting
    print("\n7. In-place sorting demonstration:")
    test_array_7 = [64, 34, 25, 12, 22, 11, 90]
    print(f"   Original: {test_array_7}")
    quicksort_inplace(test_array_7)
    print(f"   Sorted:   {test_array_7}")

    # Test case 8: Strings
    print("\n8. Sorting strings:")
    test_array_8 = ["banana", "apple", "cherry", "date"]
    print(f"   Original: {test_array_8}")
    sorted_array_8 = quicksort(test_array_8)
    print(f"   Sorted:   {sorted_array_8}")

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)
