# Reverse Even Levels Traversal Documentation

## Overview

The `reverse_even_levels()` method performs a level-order (breadth-first) traversal of a binary tree where nodes at **even-indexed levels (0, 2, 4, ...)** are reversed, while nodes at **odd-indexed levels (1, 3, 5, ...)** remain in their natural left-to-right order.

This creates an alternating pattern of directionality: even levels display right-to-left, odd levels display left-to-right.

## Algorithm

### High-Level Approach

1. **Perform Standard BFS**: Use a deque to traverse the tree level by level from root to leaves
2. **Track Level Index**: Maintain an index for each level being processed
3. **Selective Reversal**: For each level collected:
   - If the level index is **even** (0, 2, 4, ...), reverse the level using Python's slice notation `[::-1]`
   - If the level index is **odd** (1, 3, 5, ...), keep the level unchanged
4. **Return Result**: Return the list of lists with selectively reversed levels

### Pseudocode

```
function reverse_even_levels(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    level_index = 0

    while queue is not empty:
        level_size = length(queue)
        level_nodes = []

        // Process all nodes at current level
        for i = 0 to level_size - 1:
            node = queue.pop_front()
            level_nodes.append(node.value)

            if node.left exists:
                queue.append(node.left)
            if node.right exists:
                queue.append(node.right)

        // Add level to result
        if level_index is even:
            result.append(reverse(level_nodes))
        else:
            result.append(level_nodes)

        level_index++

    return result
```

### Implementation Details

**Time Complexity**: O(n)
- Each node is visited exactly once during BFS traversal
- List reversal for even levels is O(w) where w is the width of that level
- Total: O(n) since reversals are nested within the traversal

**Space Complexity**: O(w)
- Queue stores at most w nodes (where w is the maximum width/level of the tree)
- Result list is O(n) but this is output space

## Example Walkthroughs

### Example 1: Three-Level Binary Tree

**Tree Structure:**
```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

**Execution Steps:**

| Level | Index | Collected | Even? | Result |
|-------|-------|-----------|-------|--------|
| 0     | 0     | [1]       | Yes   | [1]    |
| 1     | 1     | [2, 3]    | No    | [2, 3] |
| 2     | 2     | [4, 5, 6, 7] | Yes | [7, 6, 5, 4] |

**Final Output:**
```python
[[1], [2, 3], [7, 6, 5, 4]]
```

### Example 2: Four-Level Tree with Unbalanced Right Subtree

**Tree Structure:**
```
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
    /
   8
```

**Execution Steps:**

| Level | Index | Collected | Even? | Result |
|-------|-------|-----------|-------|--------|
| 0     | 0     | [1]       | Yes   | [1]    |
| 1     | 1     | [2, 3]    | No    | [2, 3] |
| 2     | 2     | [4, 5, 6, 7] | Yes | [7, 6, 5, 4] |
| 3     | 3     | [8]       | No    | [8]    |

**Final Output:**
```python
[[1], [2, 3], [7, 6, 5, 4], [8]]
```

### Example 3: Single Node Tree

**Tree Structure:**
```
    5
```

**Execution Steps:**

| Level | Index | Collected | Even? | Result |
|-------|-------|-----------|-------|--------|
| 0     | 0     | [5]       | Yes   | [5]    |

**Note:** Single-element lists remain unchanged when reversed

**Final Output:**
```python
[[5]]
```

### Example 4: Two-Level Tree

**Tree Structure:**
```
     1
    / \
   2   3
```

**Execution Steps:**

| Level | Index | Collected | Even? | Result |
|-------|-------|-----------|-------|--------|
| 0     | 0     | [1]       | Yes   | [1]    |
| 1     | 1     | [2, 3]    | No    | [2, 3] |

**Final Output:**
```python
[[1], [2, 3]]
```

## Use Cases

### 1. Zigzag-Like Visualization
Display a tree in a zigzag pattern where alternate levels flow in opposite directions:
- Even levels: Right-to-left
- Odd levels: Left-to-right

### 2. Printer Layout
Useful for printing tree levels where every other level should be printed in reverse order for specific formatting requirements.

### 3. Graph Rendering
When rendering trees in certain visualization frameworks that require alternating directional levels.

### 4. Data Processing Pipelines
For processing tree data where even-depth nodes need different ordering than odd-depth nodes.

## Comparison with Similar Methods

### vs. level_order_traversal_left_to_right()
- **reverse_even_levels**: Even levels reversed, odd levels normal
- **level_order_traversal_left_to_right**: All levels in left-to-right order
- **Key Difference**: Selective per-level reversal

### vs. level_order_traversal_right_to_left()
- **reverse_even_levels**: Even levels reversed, odd levels normal
- **level_order_traversal_right_to_left**: All levels right-to-left
- **Key Difference**: reverse_even_levels creates alternating pattern

### vs. zigzag_level_order_traversal() (from BackwardsTree)
- **reverse_even_levels**: Even levels reversed, odd levels normal
- **zigzag_level_order_traversal**: Odd levels reversed, even levels normal (opposite!)
- **Key Difference**: The reversal pattern is inverted

## Test Coverage

The implementation includes comprehensive test coverage:

1. **Empty Tree**: Handles None root gracefully
2. **Single Node**: Tests level 0 (even) with single element
3. **Two-Level Tree**: Tests interaction between even level 0 and odd level 1
4. **Three-Level Full Binary Tree**: Standard balanced test case
5. **Four-Level Tree**: Tests multiple even-level reversals
6. **Unbalanced Left-Heavy Tree**: Tests asymmetric tree structure
7. **Unbalanced Right-Heavy Tree**: Tests right-biased tree structure

All tests verify:
- Correct level ordering (top-to-bottom)
- Correct reversal application (even levels only)
- Correct handling of edge cases
- Consistent behavior across different tree topologies

## Edge Cases Handled

| Case | Handling | Result |
|------|----------|--------|
| Empty tree | Returns empty list | `[]` |
| Single node | Level 0 is even, single element unchanged | `[[value]]` |
| All odd depths | Only odd levels collected, no reversal applied | Standard left-to-right order |
| Unbalanced tree | Processes available nodes per level | Works for any tree shape |
| Single-element levels | Reversing single element is no-op | Correctly handled |

## Implementation Characteristics

### Advantages
- **Clean separation**: Only even levels affected, easy to understand
- **Efficient**: Single pass through tree with O(n) complexity
- **Predictable**: Deterministic output pattern
- **Pythonic**: Uses list comprehension with enumerate for clarity
- **Symmetric**: Can easily be modified to reverse odd levels instead

### Limitations
- **Not recursive**: Uses iterative BFS approach
- **Memory overhead**: Stores entire tree output in memory
- **Single directional**: Cannot selectively reverse based on tree values
- **Index-based**: Depends on level index, not node properties

## Related Methods in BinaryTree

The BinaryTree class provides complementary traversal methods:

| Method | Level Order | Per-Level Reversal | Direction |
|--------|-------------|-------------------|-----------|
| `level_order_traversal_left_to_right()` | Top-to-bottom | None | Left-to-right |
| `level_order_traversal_right_to_left()` | Top-to-bottom | All | Right-to-left |
| `reverse_level_order_traversal()` | Bottom-to-top | None | Left-to-right |
| `reverse_level_order_traversal_right_to_left()` | Bottom-to-top | All | Right-to-left |
| **`reverse_even_levels()`** | **Top-to-bottom** | **Even only** | **Alternating** |

## Performance Summary

```
Method: reverse_even_levels()
├── Time Complexity: O(n)
│   ├── BFS traversal: O(n)
│   └── Reversals (nested): O(w) each, total O(n) across all levels
├── Space Complexity: O(w)
│   ├── Queue: O(w) nodes at maximum width
│   └── Result: O(n) output storage
└── Ideal Use: Level-based display with alternating directionality
```

## Code Example

```python
from tree import BinaryTree, TreeNode

# Create tree
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

tree = BinaryTree(root)
result = tree.reverse_even_levels()

# Output: [[1], [2, 3], [7, 6, 5, 4]]
print(result)

# Visualization:
# Level 0 (even):  [1]           <- reversed (no change for single element)
# Level 1 (odd):   [2, 3]        <- unchanged (left-to-right)
# Level 2 (even):  [7, 6, 5, 4]  <- reversed (was [4, 5, 6, 7])
```

## Modification Possibilities

### To Reverse Odd Levels Instead

```python
# Change the condition in the return statement
return [level[::-1] if i % 2 == 1 else level for i, level in enumerate(result)]
```

### To Reverse Every nth Level

```python
# Example: reverse every 3rd level (0, 3, 6, ...)
return [level[::-1] if i % 3 == 0 else level for i, level in enumerate(result)]
```

### To Apply Conditional Reversal

```python
# Example: reverse only wide levels
return [level[::-1] if len(level) > threshold else level for level in result]
```
