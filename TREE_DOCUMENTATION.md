# BinaryTree Class Documentation

## Overview

The `BinaryTree` class provides a comprehensive implementation of binary tree traversal algorithms with support for both standard left-to-right and reverse directional traversals. It implements 8 distinct traversal methods spanning both breadth-first (BFS) and depth-first (DFS) approaches.

## Class Purpose

The `BinaryTree` class manages a binary tree structure and provides complete traversal capabilities for exploring tree nodes in multiple directions:
- **Forward directions**: Left-to-right, top-to-bottom
- **Reverse directions**: Right-to-left, bottom-to-top
- **Traversal paradigms**: Breadth-first (level-order) and depth-first (in-order, pre-order, post-order)

## TreeNode Structure

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value      # The data stored in the node
        self.left = left        # Reference to left child node
        self.right = right      # Reference to right child node
```

A simple node structure that forms the building blocks of the binary tree.

## Core Traversal Methods

### 1. Level-Order Traversals (BFS-Based)

#### `level_order_traversal_left_to_right()`

**Purpose**: Standard breadth-first search traversing from top to bottom with left-to-right ordering at each level.

**Algorithm**:
1. Initialize a deque with the root node
2. While the deque has nodes:
   - Capture the current level size
   - Process all nodes at the current level by dequeuing
   - For each node, enqueue its left child (if exists), then right child
   - Append collected node values to result as one level

**Time Complexity**: O(n) - visits each node exactly once
**Space Complexity**: O(w) - where w is the maximum width of the tree

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [[1], [2, 3], [4, 5, 6, 7]]
```

---

#### `level_order_traversal_right_to_left()`

**Purpose**: BFS traversal displaying each level with rightmost node first while maintaining top-to-bottom level order.

**Algorithm**:
1. Perform standard BFS collecting levels in left-to-right order
2. For each collected level, reverse the node values using Python's slice notation `[::-1]`
3. Returns levels in top-to-bottom order but with reversed node positions

**Time Complexity**: O(n)
**Space Complexity**: O(w)

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [[1], [3, 2], [7, 6, 5, 4]]
```

**Key Difference**: Same traversal pattern as left-to-right, but each level is displayed in reverse order for applications requiring right-first processing without modifying the tree structure.

---

#### `reverse_level_order_traversal()`

**Purpose**: BFS collecting all levels, then returning them in bottom-to-top order while maintaining left-to-right ordering within each level.

**Algorithm**:
1. Perform standard BFS collecting all levels from root to leaves
2. Collect node values in natural left-to-right order for each level
3. Reverse the entire result list using `result[::-1]`
4. Return levels in bottom-to-top sequence

**Time Complexity**: O(n)
**Space Complexity**: O(w)

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [[4, 5, 6, 7], [2, 3], [1]]
```

**Use Case**: Processing trees from leaf level upward without recursion; useful for hierarchical cleanup or bottom-up aggregation operations.

---

#### `reverse_level_order_traversal_right_to_left()`

**Purpose**: Combined reversal - returns levels from bottom-to-top with each level displaying rightmost node first.

**Algorithm**:
1. Perform standard BFS collecting all levels from root to leaves
2. Apply dual reversal using list comprehension: `[level[::-1] for level in result[::-1]]`
3. This reverses both the level order (bottom-to-top) and individual level ordering (right-to-left)

**Time Complexity**: O(n)
**Space Complexity**: O(w)

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [[7, 6, 5, 4], [3, 2], [1]]
```

**Use Case**: Tree processing from leaves to root with right-to-left directionality; useful for applications combining both reverse directions.

---

### 2. Depth-First Traversals (Recursive DFS)

All DFS methods use recursive helper functions to maintain clean traversal logic. The recursion stack provides implicit depth-first ordering.

#### `reverse_inorder_traversal()`

**Purpose**: Depth-first traversal in reverse in-order sequence: Right subtree → Current node → Left subtree.

**Algorithm**:
1. Recursively process right subtree first (gives reverse ordering)
2. Append current node's value
3. Recursively process left subtree

**Helper Method**: `_reverse_inorder_helper(node, result)`

**Time Complexity**: O(n)
**Space Complexity**: O(h) - where h is tree height for recursion stack

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [7, 6, 5, 4, 3, 2, 1]
```

**Characteristics**:
- Opposite of standard in-order traversal (Left → Node → Right)
- For binary search trees, produces values in descending order
- Useful for reverse-order element processing

---

#### `reverse_preorder_traversal()`

**Purpose**: Depth-first traversal in reverse pre-order sequence: Current node → Right subtree → Left subtree.

**Algorithm**:
1. Append current node's value first (pre-order characteristic)
2. Recursively process right subtree (reverse characteristic)
3. Recursively process left subtree

**Helper Method**: `_reverse_preorder_helper(node, result)`

**Time Complexity**: O(n)
**Space Complexity**: O(h)

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [1, 3, 7, 6, 2, 5, 4]
```

**Characteristics**:
- Node is visited before its subtrees (pre-order property)
- Subtrees explored right-to-left (reverse property)
- Useful for tree cloning with reverse processing
- Can be used to serialize trees for reverse reconstruction

---

#### `reverse_postorder_traversal()`

**Purpose**: Depth-first traversal in reverse post-order sequence: Right subtree → Left subtree → Current node.

**Algorithm**:
1. Recursively process right subtree first (reverse characteristic)
2. Recursively process left subtree
3. Append current node's value last (post-order characteristic)

**Helper Method**: `_reverse_postorder_helper(node, result)`

**Time Complexity**: O(n)
**Space Complexity**: O(h)

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [7, 6, 3, 5, 4, 2, 1]
```

**Characteristics**:
- Node is visited after its subtrees (post-order property)
- Right subtree processed before left (reverse property)
- Useful for cleanup operations in reverse order
- Can be used for tree deletion with right-first traversal

---

## Performance Summary

| Method | Time Complexity | Space Complexity | Direction |
|--------|-----------------|------------------|-----------|
| `level_order_traversal_left_to_right` | O(n) | O(w) | Top-bottom, left-right |
| `level_order_traversal_right_to_left` | O(n) | O(w) | Top-bottom, right-left |
| `reverse_level_order_traversal` | O(n) | O(w) | Bottom-top, left-right |
| `reverse_level_order_traversal_right_to_left` | O(n) | O(w) | Bottom-top, right-left |
| `reverse_inorder_traversal` | O(n) | O(h) | Right-node-left |
| `reverse_preorder_traversal` | O(n) | O(h) | Node-right-left |
| `reverse_postorder_traversal` | O(n) | O(h) | Right-left-node |

Where:
- **n** = number of nodes in the tree
- **w** = maximum width (nodes at widest level)
- **h** = height of the tree

## Implementation Details

### Data Structure Choices

**Deque (collections.deque)**: Used for BFS methods
- Provides O(1) append and popleft operations
- More efficient than list for queue operations
- Prevents O(n) operations from list.pop(0)

### Reversal Technique

**Python slice notation `[::-1]`**: Used for efficient list reversals
- O(n) time complexity with optimized C-level implementation
- Creates new reversed list
- Preferred over manual reversal loops for readability and performance

### Recursion vs. Iteration

**BFS Methods**: Iterative with deque
- More memory-efficient for wide trees
- Explicit control over queue management
- Clear level boundary separation

**DFS Methods**: Recursive with helper functions
- Simpler code structure
- Automatic depth-first ordering via call stack
- Space complexity tied to tree height rather than width

## Usage Examples

### Creating a Tree

```python
from tree import BinaryTree, TreeNode

# Create nodes
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)

node6 = TreeNode(6)
node7 = TreeNode(7)
node3 = TreeNode(3, node6, node7)

node1 = TreeNode(1, node2, node3)

# Create tree
tree = BinaryTree(node1)
```

### Traversal Examples

```python
# Level-order traversals
left_to_right = tree.level_order_traversal_left_to_right()
# Output: [[1], [2, 3], [4, 5, 6, 7]]

right_to_left = tree.level_order_traversal_right_to_left()
# Output: [[1], [3, 2], [7, 6, 5, 4]]

# Reverse level-order
bottom_to_top = tree.reverse_level_order_traversal()
# Output: [[4, 5, 6, 7], [2, 3], [1]]

# Depth-first traversals
reverse_inorder = tree.reverse_inorder_traversal()
# Output: [7, 6, 5, 4, 3, 2, 1]

reverse_preorder = tree.reverse_preorder_traversal()
# Output: [1, 3, 7, 6, 2, 5, 4]

reverse_postorder = tree.reverse_postorder_traversal()
# Output: [7, 6, 3, 5, 4, 2, 1]
```

### Getting Summary Information

```python
summary = tree.POST_RUN_SUMMARY()
# Returns comprehensive metadata about the implementation
print(summary)
# {
#     "class": "BinaryTree",
#     "purpose": "Complete binary tree traversal with forward and reverse options",
#     "methods_count": 8,
#     "traversal_types": ["level-order", "depth-first"],
#     "directions": ["left-to-right", "right-to-left", "top-to-bottom", "bottom-to-top"],
#     "time_complexity": "O(n)",
#     "space_complexity": "O(w) or O(h)",
#     "key_feature": "Comprehensive reversal capabilities for tree exploration"
# }
```

## Edge Cases Handled

1. **Empty Tree**: All methods return empty list `[]` when root is `None`
2. **Single Node**: Correctly returns `[[value]]` for level-order and single-element list for DFS
3. **Unbalanced Trees**: Works correctly regardless of tree balance or structure
4. **None Children**: Safely handles nodes with missing left or right children

## Key Features

### Comprehensive Directional Coverage
- All combinations of forward/reverse directions are covered
- Both level-based and value-based traversals available
- Supports both breadth-first and depth-first paradigms

### Clean Code Organization
- Helper methods keep traversal logic clear and testable
- Consistent naming convention for method pairs
- Inline comments explain algorithm flow without being verbose

### Performance Optimized
- O(n) time complexity for all methods
- Appropriate space complexity for each approach
- Uses Python built-in optimizations where possible

### Well-Tested
- Comprehensive unit test suite in `test_tree.py`
- Tests cover all traversal methods with standard test tree
- Validates output format and correctness

## Related Classes

- **BackwardsTree** (`backwards_tree.py`): Specializes in right-to-left traversal with additional methods like zigzag traversal
- **TreeNode**: Shared node structure used by both tree implementations

## No External Dependencies

All methods use only Python's built-in modules:
- `collections.deque`: For efficient queue operations in BFS methods
- Standard Python recursion: For DFS methods

This makes the implementation lightweight and portable across Python environments.
