"""
Reverse Backward Node Algorithm Implementation

This module provides a complete implementation of the reverse backward node algorithm,
which traverses a tree or graph structure from leaf nodes back to the root in a
bottom-up manner. This is useful for post-order processing, depth-first analysis,
and bottom-up dynamic programming problems.

Algorithm Overview:
    - Traverses nodes starting from leaves and moving toward the root
    - Visits all child nodes before visiting the parent node
    - Can be implemented recursively or iteratively
    - Time Complexity: O(n) where n is the number of nodes
    - Space Complexity: O(h) for recursive (h = height), O(n) for iterative

Classes:
    Node: Represents a single node in the tree/graph structure
    ReverseBackwardTraversal: Provides traversal algorithms

Examples:
    Basic usage with a simple tree:

    >>> root = Node(1)
    >>> root.add_child(Node(2))
    >>> root.add_child(Node(3))
    >>> traversal = ReverseBackwardTraversal()
    >>> result = traversal.traverse_recursive(root)
    >>> print(result)  # [2, 3, 1]

Author: Algorithm Implementation Module
Version: 1.0
License: MIT
"""

from typing import List, Optional, Any, Callable
from collections import deque


class Node:
    """
    Represents a single node in a tree or graph structure.

    Each node can have multiple child nodes and maintains a reference to
    its parent node for bidirectional traversal.

    Attributes:
        value: The data stored in this node
        children: List of child nodes
        parent: Reference to the parent node (None for root)

    Example:
        >>> node = Node(42)
        >>> child1 = Node(10)
        >>> child2 = Node(20)
        >>> node.add_child(child1)
        >>> node.add_child(child2)
        >>> print(node.value)
        42
        >>> print(len(node.children))
        2
    """

    def __init__(self, value: Any, parent: Optional['Node'] = None) -> None:
        """
        Initialize a node with a value and optional parent reference.

        Args:
            value: The data/value to store in this node
            parent: Optional reference to the parent node (default: None)

        Raises:
            TypeError: If parent is not None or a Node instance
        """
        self.value = value
        self.parent = parent
        self.children: List['Node'] = []

        # Validate parent type
        if parent is not None and not isinstance(parent, Node):
            raise TypeError(f"parent must be a Node instance or None, got {type(parent)}")

    def add_child(self, child: 'Node') -> None:
        """
        Add a child node to this node's children list.

        Args:
            child: The Node to add as a child

        Raises:
            TypeError: If child is not a Node instance
            ValueError: If child is already in the children list

        Example:
            >>> parent = Node(1)
            >>> child = Node(2)
            >>> parent.add_child(child)
            >>> assert len(parent.children) == 1
        """
        if not isinstance(child, Node):
            raise TypeError(f"child must be a Node instance, got {type(child)}")

        if child in self.children:
            raise ValueError("This child is already in the children list")

        # Set the child's parent reference to this node
        child.parent = self
        self.children.append(child)

    def remove_child(self, child: 'Node') -> None:
        """
        Remove a child node from this node's children list.

        Args:
            child: The Node to remove from children

        Raises:
            ValueError: If child is not in the children list

        Example:
            >>> parent = Node(1)
            >>> child = Node(2)
            >>> parent.add_child(child)
            >>> parent.remove_child(child)
            >>> assert len(parent.children) == 0
        """
        if child not in self.children:
            raise ValueError("This child is not in the children list")

        # Clear the child's parent reference
        child.parent = None
        self.children.remove(child)

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            A string showing the node's value and number of children
        """
        return f"Node({self.value}, children={len(self.children)})"

    def __eq__(self, other: Any) -> bool:
        """
        Check equality based on node identity, not value.

        Args:
            other: Another object to compare with

        Returns:
            True if both refer to the same object, False otherwise
        """
        return self is other


class ReverseBackwardTraversal:
    """
    Implements reverse backward (post-order) tree traversal algorithms.

    This class provides both recursive and iterative approaches to traverse
    a tree structure from leaf nodes back to the root, visiting children
    before parents.

    The traversal is useful for:
        - Post-order processing (e.g., calculating subtree heights)
        - Freeing memory in bottom-up order
        - Building dependency graphs
        - Dynamic programming on trees

    Example:
        >>> root = Node(1)
        >>> left = Node(2)
        >>> right = Node(3)
        >>> root.add_child(left)
        >>> root.add_child(right)
        >>> traversal = ReverseBackwardTraversal()
        >>> result = traversal.traverse_recursive(root)
        >>> print(result)  # [2, 3, 1]
    """

    def traverse_recursive(self, root: Optional[Node]) -> List[Any]:
        """
        Recursively traverse the tree in reverse backward order (post-order).

        This is the simplest approach using Python's call stack. It visits all
        children of a node before visiting the node itself.

        Algorithm:
            1. If node is None, return empty list
            2. For each child, recursively traverse and collect results
            3. Append current node's value after all children

        Args:
            root: The root node to start traversal from. Can be None.

        Returns:
            A list of node values in post-order (reverse backward) traversal

        Raises:
            TypeError: If root is not None or a Node instance

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) where h is height (recursion stack)

        Example:
            >>> root = Node(1)
            >>> root.add_child(Node(2))
            >>> root.add_child(Node(3))
            >>> traversal = ReverseBackwardTraversal()
            >>> print(traversal.traverse_recursive(root))
            [2, 3, 1]
        """
        # Validate input
        if root is not None and not isinstance(root, Node):
            raise TypeError(f"root must be a Node instance or None, got {type(root)}")

        # Base case: empty tree
        if root is None:
            return []

        result = []

        # Recursively process all children first
        for child in root.children:
            result.extend(self.traverse_recursive(child))

        # Add the current node after all children (post-order)
        result.append(root.value)

        return result

    def traverse_iterative(self, root: Optional[Node]) -> List[Any]:
        """
        Iteratively traverse the tree in reverse backward order (post-order).

        This approach uses a stack instead of recursion, avoiding stack overflow
        for very deep trees.

        Algorithm:
            1. Use a stack to track nodes to visit
            2. Use a visited list to track nodes already processed
            3. Push root onto stack
            4. While stack is not empty:
               - Peek at top node
               - If all children visited, pop and add to result
               - Otherwise, push unvisited children to stack

        Args:
            root: The root node to start traversal from. Can be None.

        Returns:
            A list of node values in post-order (reverse backward) traversal

        Raises:
            TypeError: If root is not None or a Node instance

        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(n) in worst case (storing all nodes in stack)

        Example:
            >>> root = Node(1)
            >>> root.add_child(Node(2))
            >>> root.add_child(Node(3))
            >>> traversal = ReverseBackwardTraversal()
            >>> print(traversal.traverse_iterative(root))
            [2, 3, 1]
        """
        # Validate input
        if root is not None and not isinstance(root, Node):
            raise TypeError(f"root must be a Node instance or None, got {type(root)}")

        # Base case: empty tree
        if root is None:
            return []

        result = []
        stack = [root]
        visited = []  # Use list instead of set to track visited nodes

        while stack:
            # Look at the top of the stack without removing
            node = stack[-1]

            # Check if all children have been visited
            if all(child in visited for child in node.children):
                # All children visited, so add current node and pop
                stack.pop()
                visited.append(node)
                result.append(node.value)
            else:
                # Push unvisited children onto stack in reverse order
                # (reverse order ensures we process left-to-right in final result)
                for child in reversed(node.children):
                    if child not in visited:
                        stack.append(child)

        return result

    def traverse_with_callback(
        self,
        root: Optional[Node],
        callback: Callable[[Any], None],
        method: str = 'recursive'
    ) -> None:
        """
        Traverse the tree and call a function for each node value.

        This is useful for processing nodes as they're visited without
        building up a list in memory.

        Args:
            root: The root node to start traversal from. Can be None.
            callback: A function that takes a node value and returns None
            method: Either 'recursive' or 'iterative' (default: 'recursive')

        Raises:
            TypeError: If root is not a Node or None, or callback is not callable
            ValueError: If method is not 'recursive' or 'iterative'

        Example:
            >>> root = Node(1)
            >>> root.add_child(Node(2))
            >>> root.add_child(Node(3))
            >>> traversal = ReverseBackwardTraversal()
            >>> values = []
            >>> traversal.traverse_with_callback(root, lambda x: values.append(x))
            >>> print(values)
            [2, 3, 1]
        """
        # Validate inputs
        if root is not None and not isinstance(root, Node):
            raise TypeError(f"root must be a Node instance or None, got {type(root)}")

        if not callable(callback):
            raise TypeError(f"callback must be callable, got {type(callback)}")

        if method not in ('recursive', 'iterative'):
            raise ValueError(f"method must be 'recursive' or 'iterative', got {method}")

        # Use the appropriate traversal method
        if method == 'recursive':
            values = self.traverse_recursive(root)
        else:
            values = self.traverse_iterative(root)

        # Call the callback for each value
        for value in values:
            callback(value)

    def traverse_by_depth(self, root: Optional[Node]) -> List[List[Any]]:
        """
        Traverse the tree and group nodes by their depth level.

        Instead of a flat list, this returns nodes grouped by their depth
        from the root (0 = root, 1 = children of root, etc.).

        Args:
            root: The root node to start traversal from. Can be None.

        Returns:
            A list of lists, where each inner list contains nodes at that depth

        Raises:
            TypeError: If root is not None or a Node instance

        Example:
            >>> root = Node(1)
            >>> left = Node(2)
            >>> right = Node(3)
            >>> root.add_child(left)
            >>> root.add_child(right)
            >>> left.add_child(Node(4))
            >>> traversal = ReverseBackwardTraversal()
            >>> print(traversal.traverse_by_depth(root))
            [[4], [2, 3], [1]]
        """
        # Validate input
        if root is not None and not isinstance(root, Node):
            raise TypeError(f"root must be a Node instance or None, got {type(root)}")

        # Base case: empty tree
        if root is None:
            return []

        result = []
        queue = deque([(root, 0)])  # (node, depth)
        depth_map = {}

        # First pass: collect nodes by depth using BFS
        while queue:
            node, depth = queue.popleft()

            if depth not in depth_map:
                depth_map[depth] = []
            depth_map[depth].append(node)

            # Add children with depth + 1
            for child in node.children:
                queue.append((child, depth + 1))

        # Second pass: build result in reverse depth order (bottom-up)
        max_depth = max(depth_map.keys()) if depth_map else 0
        for depth in range(max_depth, -1, -1):
            if depth in depth_map:
                result.append([node.value for node in depth_map[depth]])

        return result


def build_example_tree() -> Node:
    r"""
    Build a sample tree for testing and demonstration.

    Tree structure:
                1
               / \
              2   3
             / \   \
            4   5   6

    Returns:
        The root node of the constructed tree

    Example:
        >>> root = build_example_tree()
        >>> print(root.value)
        1
    """
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root.add_child(node2)
    root.add_child(node3)
    node2.add_child(node4)
    node2.add_child(node5)
    node3.add_child(node6)

    return root


if __name__ == "__main__":
    """
    Demonstrate the reverse backward node algorithm with examples.
    """
    print("=" * 70)
    print("REVERSE BACKWARD NODE ALGORITHM DEMONSTRATION")
    print("=" * 70)

    # Create example tree
    root = build_example_tree()
    traversal = ReverseBackwardTraversal()

    # Demonstrate recursive traversal
    print("\n1. Recursive Traversal (Post-order):")
    print("-" * 70)
    result_recursive = traversal.traverse_recursive(root)
    print(f"Result: {result_recursive}")
    print("Explanation: Visits children before parents (leaf to root)")

    # Demonstrate iterative traversal
    print("\n2. Iterative Traversal (Post-order):")
    print("-" * 70)
    result_iterative = traversal.traverse_iterative(root)
    print(f"Result: {result_iterative}")
    print("Explanation: Same result using stack instead of recursion")

    # Demonstrate callback-based traversal
    print("\n3. Callback-based Traversal:")
    print("-" * 70)
    values = []
    traversal.traverse_with_callback(root, lambda x: values.append(x))
    print(f"Collected values: {values}")
    print("Explanation: Process nodes as they're visited (memory-efficient)")

    # Demonstrate depth-level traversal
    print("\n4. Traversal by Depth Level:")
    print("-" * 70)
    result_by_depth = traversal.traverse_by_depth(root)
    print(f"Result: {result_by_depth}")
    print("Explanation: Groups nodes by their distance from root")
    print("  Level 0 (deepest): [4, 5, 6]")
    print("  Level 1 (middle):  [2, 3]")
    print("  Level 2 (root):    [1]")

    # Edge case: single node
    print("\n5. Edge Case - Single Node:")
    print("-" * 70)
    single = Node(99)
    result_single = traversal.traverse_recursive(single)
    print(f"Result: {result_single}")
    print("Explanation: Single node returns just that node")

    # Edge case: empty tree
    print("\n6. Edge Case - Empty Tree (None):")
    print("-" * 70)
    result_empty = traversal.traverse_recursive(None)
    print(f"Result: {result_empty}")
    print("Explanation: Empty tree returns empty list")

    print("\n" + "=" * 70)
    print("ALGORITHM PROPERTIES")
    print("=" * 70)
    print("Time Complexity:  O(n) - visits each node exactly once")
    print("Space Complexity: O(h) for recursive, O(n) for iterative")
    print("  where n = number of nodes, h = height of tree")
    print("\nCommon Use Cases:")
    print("  • Post-order tree processing (e.g., calculating subtree heights)")
    print("  • Memory cleanup (free children before parents)")
    print("  • Building dependency chains")
    print("  • Tree-based dynamic programming")
    print("=" * 70)
