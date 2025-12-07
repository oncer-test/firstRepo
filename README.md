# Binary Tree Traversal Implementation

Comprehensive implementation of binary tree traversal algorithms with both forward and reverse directional capabilities.

## Overview

This project provides two main classes for tree traversal:
- **BinaryTree**: Standard left-to-right tree traversal with reverse options
- **BackwardsTree**: Right-to-left and bidirectional tree traversal operations

## BinaryTree Class

The `BinaryTree` class implements 8 distinct traversal methods supporting forward and reverse directions:

### Level-Order Traversals (BFS-based)
- **level_order_traversal_left_to_right**: Top-to-bottom, left-to-right per level
  - Uses deque with standard left-child-first enqueuing
  - Time: O(n), Space: O(w)
  - Returns: `[[1], [2, 3], [4, 5, 6, 7]]`

- **level_order_traversal_right_to_left**: Top-to-bottom, right-to-left per level
  - Collects left-to-right but reverses each level for display
  - Time: O(n), Space: O(w)
  - Returns: `[[1], [3, 2], [7, 6, 5, 4]]`

- **reverse_level_order_traversal**: Bottom-to-top, left-to-right per level
  - Reverses entire level list after BFS collection
  - Time: O(n), Space: O(w)
  - Returns: `[[4, 5, 6, 7], [2, 3], [1]]`

- **reverse_level_order_traversal_right_to_left**: Bottom-to-top, right-to-left per level
  - Combines full list reversal with individual level reversal
  - Time: O(n), Space: O(w)
  - Returns: `[[7, 6, 5, 4], [3, 2], [1]]`

### Depth-First Traversals (Recursive DFS)
- **reverse_inorder_traversal**: Right → Node → Left
  - Reverse of standard inorder (Left → Node → Right)
  - Time: O(n), Space: O(h)
  - Returns: `[7, 6, 5, 4, 3, 2, 1]`

- **reverse_preorder_traversal**: Node → Right → Left
  - Processes node first with right-biased subtree exploration
  - Time: O(n), Space: O(h)
  - Returns: `[1, 3, 7, 6, 2, 5, 4]`

- **reverse_postorder_traversal**: Right → Left → Node
  - Processes node last with right-biased subtree exploration
  - Time: O(n), Space: O(h)
  - Returns: `[7, 6, 3, 5, 4, 2, 1]`

## BackwardsTree Class

The `BackwardsTree` class specializes in right-to-left and bidirectional traversals with 6 methods:

### Level-Order Traversals (BFS-based)
- **level_order_traversal_right_to_left**: Top-to-bottom, right-to-left per level
  - Adds right children before left children in queue
  - Time: O(n), Space: O(w)
  - Returns: `[[1], [3, 2], [7, 6, 5, 4]]`

- **reverse_level_order_traversal_right_to_left**: Bottom-to-top, right-to-left per level
  - Combines BFS right-biased collection with level order reversal
  - Time: O(n), Space: O(w)
  - Returns: `[[7, 6, 5, 4], [3, 2], [1]]`

- **zigzag_level_order_traversal**: Alternating directional levels
  - Even levels (0,2,4...): left-to-right
  - Odd levels (1,3,5...): right-to-left
  - Time: O(n), Space: O(w)
  - Returns: `[[1], [3, 2], [4, 5, 6, 7]]`

### Depth-First Traversals (DFS with right-bias)
- **reverse_inorder_traversal_right_to_left**: Right → Node → Left
- **reverse_preorder_traversal_right_to_left**: Node → Right → Left
- **reverse_postorder_traversal_right_to_left**: Right → Left → Node

All DFS methods have Time: O(n), Space: O(h)

## Example Tree Structure

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

## Key Implementation Details

- **BFS Methods**: Use Python's `deque` for O(1) append/popleft operations
- **DFS Methods**: Recursive implementation with clean separation of concerns
- **List Operations**: Python's optimized slice notation `[::-1]` for reversals in O(n)
- **Child Ordering**: Right-child-first insertion determines traversal direction in BackwardsTree
- **No External Dependencies**: Uses only Python's built-in `collections` module

## Usage

```python
from tree import TreeNode, BinaryTree
from backwards_tree import BackwardsTree

# Create a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# BinaryTree traversals
tree = BinaryTree(root)
print(tree.level_order_traversal_left_to_right())  # [[1], [2, 3], [4, 5, 6, 7]]
print(tree.reverse_inorder_traversal())             # [7, 6, 5, 4, 3, 2, 1]

# BackwardsTree traversals
btree = BackwardsTree(root)
print(btree.level_order_traversal_right_to_left())  # [[1], [3, 2], [7, 6, 5, 4]]
print(btree.zigzag_level_order_traversal())         # [[1], [3, 2], [4, 5, 6, 7]]
```

## Performance Summary

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| Level-Order (BFS) | O(n) | O(w) | Level-by-level processing |
| Reverse Level | O(n) | O(w) | Leaf-to-root processing |
| Zigzag | O(n) | O(w) | Alternating direction processing |
| In-Order DFS | O(n) | O(h) | Sorted traversal (BST) |
| Pre-Order DFS | O(n) | O(h) | Tree copying/serialization |
| Post-Order DFS | O(n) | O(h) | Tree deletion/cleanup |

Where:
- n = number of nodes
- w = maximum tree width (nodes at widest level)
- h = tree height (distance from root to farthest leaf)
