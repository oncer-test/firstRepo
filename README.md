# Reverse Backward Node Algorithm

A complete Python implementation of the **reverse backward (post-order) tree traversal algorithm** with comprehensive documentation, tests, and examples.

## Overview

This project provides a robust implementation of tree/graph traversal that visits nodes from leaves to root (bottom-up). This is essential for many algorithms including post-order processing, dynamic programming on trees, and resource cleanup.

## Features

- ✅ **Node Class**: Tree/graph structure representation with parent-child relationships
- ✅ **Recursive Traversal**: Classic recursive implementation with minimal overhead
- ✅ **Iterative Traversal**: Stack-based approach avoiding recursion depth limits
- ✅ **Callback-based Traversal**: Memory-efficient processing with custom callbacks
- ✅ **Depth-level Grouping**: Analyze nodes by their distance from root
- ✅ **Comprehensive Documentation**: Detailed docstrings for all public APIs
- ✅ **Full Test Suite**: 40+ unit tests covering all scenarios
- ✅ **Real-world Examples**: 7 practical demonstration examples

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd firstRepo

# No external dependencies required - pure Python implementation
```

### Basic Usage

```python
from src.reverse_backward_node import Node, ReverseBackwardTraversal

# Create a tree
root = Node(1)
left = Node(2)
right = Node(3)
root.add_child(left)
root.add_child(right)

# Traverse in post-order (reverse backward)
traversal = ReverseBackwardTraversal()
result = traversal.traverse_recursive(root)
print(result)  # Output: [2, 3, 1]
```

## Algorithm Details

### What is Reverse Backward Traversal?

Post-order (reverse backward) traversal visits nodes in this order:
1. **Recursively visit all children**
2. **Then visit the parent**

This ensures child nodes are processed before their parents.

### Tree Example

```
       1
      / \
     2   3
    / \
   4   5

Post-order: [4, 5, 2, 3, 1]
```

### Complexity Analysis

| Metric | Value | Notes |
|--------|-------|-------|
| **Time Complexity** | O(n) | Each node visited exactly once |
| **Space Complexity (Recursive)** | O(h) | h = height of tree (call stack) |
| **Space Complexity (Iterative)** | O(n) | Using explicit stack storage |

## Project Structure

```
.
├── src/
│   ├── __init__.py                    # Package initialization
│   └── reverse_backward_node.py       # Main algorithm implementation (450+ lines)
├── tests/
│   └── test_reverse_backward_node.py # 40+ comprehensive unit tests
├── examples/
│   └── example_usage.py               # 7 real-world example scenarios
├── README.md                          # This file
├── LICENSE                            # MIT License
└── .gitignore                         # Git ignore patterns
```

## API Reference

### Node Class

```python
class Node:
    """Represents a single node in the tree/graph."""

    def __init__(self, value, parent=None)
    def add_child(child: Node) -> None
    def remove_child(child: Node) -> None
```

**Example:**
```python
node = Node(42)
child = Node(10)
node.add_child(child)
print(len(node.children))  # 1
```

### ReverseBackwardTraversal Class

```python
class ReverseBackwardTraversal:
    """Implements post-order tree traversal algorithms."""

    def traverse_recursive(root: Optional[Node]) -> List[Any]
    def traverse_iterative(root: Optional[Node]) -> List[Any]
    def traverse_with_callback(root, callback, method='recursive') -> None
    def traverse_by_depth(root: Optional[Node]) -> List[List[Any]]
```

**Method Details:**

#### traverse_recursive()
- **Best for**: Simple trees, when recursion depth is acceptable
- **Time**: O(n) | **Space**: O(h)
- **Example**: `result = traversal.traverse_recursive(root)`

#### traverse_iterative()
- **Best for**: Very deep trees (avoids stack overflow)
- **Time**: O(n) | **Space**: O(n)
- **Example**: `result = traversal.traverse_iterative(root)`

#### traverse_with_callback()
- **Best for**: Large trees, memory-constrained environments
- **Time**: O(n) | **Space**: O(h) or O(n) depending on method
- **Example**: `traversal.traverse_with_callback(root, print)`

#### traverse_by_depth()
- **Best for**: Level-by-level analysis
- **Returns**: Nodes grouped by depth (bottom-up)
- **Example**: `by_depth = traversal.traverse_by_depth(root)`

## Usage Examples

### Example 1: Simple Tree Traversal

```python
root = Node("Root")
root.add_child(Node("Child 1"))
root.add_child(Node("Child 2"))

traversal = ReverseBackwardTraversal()
result = traversal.traverse_recursive(root)
print(result)  # ["Child 1", "Child 2", "Root"]
```

### Example 2: File System Cleanup

```python
# Post-order is ideal for cleanup - delete children before parents
traversal = ReverseBackwardTraversal()
traversal.traverse_with_callback(
    root_dir,
    callback=cleanup_resource,
    method='iterative'
)
```

### Example 3: Computing Tree Heights

```python
def compute_height(node):
    if not node.children:
        return 0
    return 1 + max(compute_height(child) for child in node.children)

# Use post-order to compute heights efficiently
height = compute_height(root)
```

## Running Tests

```bash
# Run all unit tests
python tests/test_reverse_backward_node.py

# Run with verbose output
python -m pytest tests/test_reverse_backward_node.py -v
```

### Test Coverage

- ✅ Node creation and manipulation (7 tests)
- ✅ Recursive traversal (7 tests)
- ✅ Iterative traversal (6 tests)
- ✅ Callback-based traversal (5 tests)
- ✅ Depth-level grouping (5 tests)
- ✅ Complex scenarios (3 tests)
- ✅ Edge cases (5 tests)

**Total: 40+ tests covering all code paths**

## Running Examples

```bash
# Run all demonstration examples
python examples/example_usage.py
```

### Available Examples

1. **Basic Tree Construction** - Simple tree creation and traversal
2. **File System Traversal** - Directory structure and cleanup
3. **Expression Tree Evaluation** - Post-order mathematical expressions
4. **Subtree Heights** - Computing tree properties
5. **Memory Cleanup** - Resource management patterns
6. **Iterative vs Recursive** - Performance and approach comparison
7. **Depth Grouping** - Level-by-level node analysis

## Use Cases

### When to Use Post-Order Traversal

- 📁 **File System Operations** - Delete directories (children before parent)
- 🎯 **Tree Cleanup** - Free memory/resources bottom-up
- 📊 **Dependency Graphs** - Process dependencies before dependents
- 🔢 **Expression Evaluation** - Evaluate operands before operators
- 🌳 **Tree DP** - Dynamic programming on trees
- 📈 **Subtree Calculations** - Heights, sizes, weights

### Example: Freeing Tree Memory

```python
def free_tree(node):
    if node is None:
        return
    # Free children first (post-order)
    for child in node.children:
        free_tree(child)
    # Then free the node itself
    del node
```

## Documentation

All code is thoroughly documented with:

- **Module docstrings**: Explain purpose and usage
- **Class docstrings**: Detail attributes and methods
- **Function docstrings**: Include Args, Returns, Raises, Examples, Time/Space complexity
- **Inline comments**: Explain complex logic and algorithms
- **Type hints**: Full type annotations for clarity

## Performance Characteristics

### Recursive Implementation
```
Time:  O(n) - single pass through all n nodes
Space: O(h) - call stack depth equals tree height
```

**Good for**: Shallow trees, clean code preference

### Iterative Implementation
```
Time:  O(n) - single pass through all n nodes
Space: O(n) - explicit stack can grow to n nodes
```

**Good for**: Deep trees, avoiding recursion limits

## Error Handling

The implementation includes comprehensive error checking:

```python
# Type validation
try:
    node = Node(1, parent="invalid")  # TypeError
except TypeError as e:
    print(f"Error: {e}")

# Value validation
try:
    parent.add_child(parent)  # ValueError (duplicate)
except ValueError as e:
    print(f"Error: {e}")

# Method validation
try:
    traversal.traverse_with_callback(root, print, method="invalid")
except ValueError as e:
    print(f"Error: {e}")
```

## Requirements

- **Python**: 3.7 or higher
- **Dependencies**: None (pure Python standard library only)

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## Version History

- **v1.0** (2025-12-06) - Initial release
  - Node class with parent-child relationships
  - Recursive and iterative post-order traversal
  - Callback-based traversal
  - Depth-level grouping
  - Comprehensive documentation and tests

## FAQ

**Q: Why use post-order instead of pre-order or in-order?**
A: Post-order is ideal when parent nodes depend on results from child nodes (e.g., computing heights, cleanup operations).

**Q: Should I use recursive or iterative?**
A: Use recursive for simpler code (most trees). Use iterative for very deep trees (100+ levels) to avoid stack overflow.

**Q: Can I modify nodes during traversal?**
A: Avoid structural changes (adding/removing children) during traversal. It's safe to modify node values.

**Q: What's the maximum tree size I can handle?**
A: Limited by available memory. Recursive method limited by Python's recursion depth (~1000 levels). Use iterative for deeper trees.

## Additional Resources

- **Algorithm Visualization**: See examples/ directory for visual tree structures
- **Test Cases**: See tests/ directory for comprehensive usage patterns
- **Source Code**: See src/reverse_backward_node.py for detailed implementation
- **Theory**: Post-order traversal is fundamental to many algorithms:
  - Tree DP (dynamic programming)
  - Graph traversal
  - Expression evaluation
  - Compiler design (AST processing)

---

**Author**: Algorithm Implementation Module
**License**: MIT
**Last Updated**: 2025-12-06
