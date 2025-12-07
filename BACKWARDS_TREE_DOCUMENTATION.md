# BackwardsTree Class Documentation

## Overview

The `BackwardsTree` class specializes in right-to-left and bidirectional binary tree traversal operations. It provides 6 distinct traversal methods that prioritize right-to-left exploration and includes a unique zigzag pattern traversal for alternating directional processing at different tree levels.

## Class Purpose

The `BackwardsTree` class manages a binary tree with a focus on reverse directionality and right-biased exploration. It complements the standard `BinaryTree` class by implementing:
- **Right-to-left processing**: Node exploration from rightmost to leftmost
- **Bidirectional approaches**: Zigzag patterns alternating between directions
- **Right-bias implementation**: Right children processed before left children
- **Reverse-order traversal**: Bottom-to-top with right-to-left directionality

## TreeNode Structure

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value      # The data stored in the node
        self.left = left        # Reference to left child node
        self.right = right      # Reference to right child node
```

A simple node structure shared with the `BinaryTree` class, enabling compatibility between both implementations.

## Core Traversal Methods

### 1. Level-Order Traversals (BFS-Based)

#### `level_order_traversal_right_to_left()`

**Purpose**: Breadth-first search traversing from top to bottom with right-to-left ordering at each level.

**Algorithm**:
1. Initialize a deque with the root node
2. While the deque has nodes:
   - Capture the current level size
   - Process all nodes at the current level by dequeuing
   - For each node, enqueue its **right child first**, then left child (key difference from standard BFS)
   - Append collected node values to result as one level
3. Natural right-to-left ordering achieved through child enqueue order

**Time Complexity**: O(n) - visits each node exactly once
**Space Complexity**: O(w) - where w is the maximum width of the tree

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [[1], [3, 2], [7, 6, 5, 4]]
```

**Key Innovation**: By enqueuing right children before left children, the traversal naturally produces right-to-left ordering without requiring post-processing list reversal. This approach is more efficient than collecting left-to-right and reversing afterward.

---

#### `reverse_level_order_traversal_right_to_left()`

**Purpose**: BFS with right-to-left level ordering AND bottom-to-top level sequence ordering.

**Algorithm**:
1. Perform BFS with right-child-first enqueuing (same as `level_order_traversal_right_to_left`)
2. Collect all levels with right-to-left node ordering
3. Reverse the entire result list using `result[::-1]`
4. Return levels in bottom-to-top sequence with right-to-left node ordering

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

**Use Case**: Applications requiring simultaneous bottom-to-top level processing AND right-to-left node ordering; useful for reverse perspective tree analysis and right-aligned hierarchical processing.

---

#### `zigzag_level_order_traversal()`

**Purpose**: Alternating directional level-order traversal - even levels left-to-right, odd levels right-to-left.

**Algorithm**:
1. Initialize deque with root and level counter at 0
2. While deque has nodes:
   - Capture current level size
   - Process all nodes at this level by dequeuing (left-to-right arrival in queue)
   - Add left child, then right child to queue (standard order)
   - Check if current level is odd using `level % 2 == 1`
   - If odd, reverse the level_nodes list using `level_nodes.reverse()`
   - Otherwise, leave level_nodes in original left-to-right order
   - Increment level counter
3. Return levels with alternating directional ordering

**Time Complexity**: O(n)
**Space Complexity**: O(w)

**Example Output**:
```
Tree:        1
           /   \
          2     3
         / \   / \
        4   5 6   7

Result: [[1], [3, 2], [4, 5, 6, 7]]

Level 0 (even): [1] - left-to-right
Level 1 (odd): [3, 2] - right-to-left (reversed)
Level 2 (even): [4, 5, 6, 7] - left-to-right
```

**Characteristics**:
- Creates a "zigzag" visual pattern when visualized
- Useful for snake-like or wave-like tree processing
- Common in applications requiring alternating read directions
- Level indexing starts at 0 (root is even)

**Use Cases**:
- Document scanning in zigzag pattern (alternating left-right, right-left)
- Printer output formatting with alternating directionality
- Game board traversal with snake pattern
- Bidirectional queue applications

---

### 2. Depth-First Traversals (Recursive DFS with Right-Bias)

All DFS methods use recursive helper functions with right-first child processing, implementing a consistent right-to-left bias throughout the tree exploration.

#### `reverse_inorder_traversal_right_to_left()`

**Purpose**: Depth-first traversal with right-to-left bias: Right subtree → Current node → Left subtree.

**Algorithm**:
1. Recursively process right subtree first (establishes right-to-left direction)
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
- Produces reverse-sorted order for binary search trees
- Traversal direction flows from right to left subtrees
- For balanced trees, processes nodes from highest to lowest values
- Equivalent to reverse in-order but using right-first approach

---

#### `reverse_preorder_traversal_right_to_left()`

**Purpose**: Depth-first traversal with right-to-left bias: Current node → Right subtree → Left subtree.

**Algorithm**:
1. Append current node's value first (pre-order characteristic)
2. Recursively process right subtree (right-to-left direction)
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

**Processing Order Breakdown**:
- Visit 1 (root)
- Process right subtree [3, 7, 6]: Visit 3, then 7, then 6
- Process left subtree [2, 5, 4]: Visit 2, then 5, then 4

**Characteristics**:
- Root visited first (pre-order property)
- Right subtree explored before left (right-to-left property)
- Can be used to create a "right-first" tree copy
- Serialization format reflects right-biased tree structure

---

#### `reverse_postorder_traversal_right_to_left()`

**Purpose**: Depth-first traversal with right-to-left bias: Right subtree → Left subtree → Current node.

**Algorithm**:
1. Recursively process right subtree first (right-to-left direction)
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

**Processing Order Breakdown**:
- Process right subtree [3]: recursively visits 7, 6, then 3
- Process left subtree [2]: recursively visits 5, 4, then 2
- Visit 1 (root last)

**Characteristics**:
- Root visited last (post-order property)
- Right subtree explored before left (right-to-left property)
- Ideal for cleanup/deletion operations with right-first preference
- Can be used for right-to-left tree dismantling

---

## Performance Summary

| Method | Time Complexity | Space Complexity | Primary Direction |
|--------|-----------------|------------------|-------------------|
| `level_order_traversal_right_to_left` | O(n) | O(w) | Right-to-left per level |
| `reverse_level_order_traversal_right_to_left` | O(n) | O(w) | Bottom-top, right-left |
| `reverse_inorder_traversal_right_to_left` | O(n) | O(h) | Right → Node → Left |
| `reverse_preorder_traversal_right_to_left` | O(n) | O(h) | Node → Right → Left |
| `reverse_postorder_traversal_right_to_left` | O(n) | O(h) | Right → Left → Node |
| `zigzag_level_order_traversal` | O(n) | O(w) | Alternating per level |

Where:
- **n** = number of nodes in the tree
- **w** = maximum width (nodes at widest level)
- **h** = height of the tree

## Implementation Details

### Right-Bias Strategy

The key architectural decision in `BackwardsTree` is **consistently processing right children before left children**:

**Benefits**:
1. Natural right-to-left ordering without post-processing reversals
2. More intuitive for applications with right-to-left requirements
3. Single-pass processing (no separate reversal step needed in most cases)
4. Reduced memory overhead by avoiding intermediate reversed lists

**Implementation Pattern**:
```python
# BFS approach
if node.right:
    queue.append(node.right)  # Right first
if node.left:
    queue.append(node.left)   # Then left

# DFS approach
self._helper(node.right, result)  # Right first
self._helper(node.left, result)   # Then left
```

### Data Structure Choices

**Deque (collections.deque)**: Used for BFS methods
- Provides O(1) append and popleft operations
- Efficient for right-child-first enqueuing
- Maintains consistent performance regardless of tree width

### Zigzag Implementation

The zigzag traversal uses a **level parity check** rather than post-processing:
- `level % 2 == 1` identifies odd levels (requiring reversal)
- Even levels (0, 2, 4...) use natural left-to-right arrival order
- Odd levels (1, 3, 5...) reverse for right-to-left order
- Level counter increments with each level processed

## Usage Examples

### Creating a Tree

```python
from backwards_tree import BackwardsTree, TreeNode

# Create nodes
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)

node6 = TreeNode(6)
node7 = TreeNode(7)
node3 = TreeNode(3, node6, node7)

node1 = TreeNode(1, node2, node3)

# Create backwards tree
tree = BackwardsTree(node1)
```

### Traversal Examples

```python
# Right-to-left level order
right_to_left = tree.level_order_traversal_right_to_left()
# Output: [[1], [3, 2], [7, 6, 5, 4]]

# Reverse level order (bottom-to-top, right-to-left)
bottom_to_top_rtl = tree.reverse_level_order_traversal_right_to_left()
# Output: [[7, 6, 5, 4], [3, 2], [1]]

# Zigzag traversal
zigzag = tree.zigzag_level_order_traversal()
# Output: [[1], [3, 2], [4, 5, 6, 7]]

# Depth-first traversals with right-bias
reverse_inorder = tree.reverse_inorder_traversal_right_to_left()
# Output: [7, 6, 5, 4, 3, 2, 1]

reverse_preorder = tree.reverse_preorder_traversal_right_to_left()
# Output: [1, 3, 7, 6, 2, 5, 4]

reverse_postorder = tree.reverse_postorder_traversal_right_to_left()
# Output: [7, 6, 3, 5, 4, 2, 1]
```

### Getting Summary Information

```python
summary = tree.POST_RUN_SUMMARY()
# Returns comprehensive metadata about the implementation
print(summary)
# {
#     "class": "BackwardsTree",
#     "purpose": "Right-to-left and bidirectional tree traversal operations",
#     "methods_count": 6,
#     "traversal_types": ["level-order", "depth-first", "zigzag"],
#     "primary_directions": ["right-to-left", "bottom-to-top", "alternating"],
#     "time_complexity": "O(n)",
#     "space_complexity": "O(w) or O(h)",
#     "key_feature": "Right-biased and reverse-order tree exploration"
# }
```

## Edge Cases Handled

1. **Empty Tree**: All methods return empty list `[]` when root is `None`
2. **Single Node**: Correctly returns `[[value]]` for level-order and single-element list for DFS
3. **Unbalanced Trees**: Works correctly regardless of tree balance or structure
4. **None Children**: Safely handles nodes with missing left or right children
5. **Odd-Level Zigzag**: Correctly reverses at odd level indices (1, 3, 5...)
6. **Single-Level Tree**: Zigzag treats root (level 0) as even and processes left-to-right

## Key Features

### Right-First Architecture
- All methods consistently process right children before left
- Natural right-to-left ordering without requiring reversals
- Clean, predictable behavior across all traversal methods

### Bidirectional Support
- Combines right-to-left processing with level reversals
- Zigzag traversal provides alternating directionality
- Flexible directional control for varied application needs

### Efficient Implementation
- O(n) time complexity for all methods
- O(w) or O(h) space complexity depending on approach
- Single-pass processing where possible
- Minimal intermediate data structure overhead

### Well-Tested
- Comprehensive unit test suite in `test_tree.py`
- Tests validate all 6 traversal methods
- Edge cases covered for unbalanced trees

## Comparison with BinaryTree

| Aspect | BinaryTree | BackwardsTree |
|--------|-----------|---------------|
| **Primary Direction** | Left-to-right | Right-to-left |
| **Methods Count** | 8 | 6 |
| **Special Features** | All direction combinations | Zigzag pattern |
| **Child Processing Order** | Left first | Right first |
| **Level Ordering** | Natural LTR or reversed | Natural RTL |
| **Use Case** | Standard forward traversal | Reverse/mirror analysis |

Both classes complement each other:
- **BinaryTree**: For forward-looking applications and all directional combinations
- **BackwardsTree**: For backward-focused, right-biased, and zigzag requirements

## Related Classes

- **BinaryTree** (`tree.py`): Implements left-to-right biased traversals with all directional options
- **TreeNode**: Shared node structure used by both tree implementations

## No External Dependencies

All methods use only Python's built-in modules:
- `collections.deque`: For efficient queue operations in BFS methods
- Standard Python recursion: For DFS methods

This makes the implementation lightweight, portable, and suitable for any Python environment without additional package requirements.
