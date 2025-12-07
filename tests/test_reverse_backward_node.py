"""
Unit tests for the Reverse Backward Node Algorithm implementation.

Tests cover:
    - Node class functionality (creation, adding/removing children)
    - Recursive traversal algorithm
    - Iterative traversal algorithm
    - Callback-based traversal
    - Depth-level traversal
    - Edge cases (empty trees, single nodes, deep trees)
    - Error handling and validation
"""

import sys
import unittest
from typing import List

# Add src directory to path for imports
sys.path.insert(0, '/Users/altyni/oncer/.local-workspaces/1a8c00d2-2cac-4232-8d16-7f452de83d30')

from src.reverse_backward_node import (
    Node,
    ReverseBackwardTraversal,
    build_example_tree,
)


class TestNodeClass(unittest.TestCase):
    """Test cases for the Node class."""

    def test_node_creation(self):
        """Test creating a basic node."""
        node = Node(42)
        self.assertEqual(node.value, 42)
        self.assertIsNone(node.parent)
        self.assertEqual(len(node.children), 0)

    def test_node_with_parent(self):
        """Test creating a node with a parent reference."""
        parent = Node(1)
        child = Node(2, parent=parent)
        self.assertEqual(child.parent, parent)
        self.assertEqual(child.value, 2)

    def test_add_child(self):
        """Test adding a child to a node."""
        parent = Node(1)
        child = Node(2)
        parent.add_child(child)

        self.assertEqual(len(parent.children), 1)
        self.assertIn(child, parent.children)
        self.assertEqual(child.parent, parent)

    def test_add_multiple_children(self):
        """Test adding multiple children to a node."""
        parent = Node(1)
        children = [Node(i) for i in range(2, 5)]

        for child in children:
            parent.add_child(child)

        self.assertEqual(len(parent.children), 3)
        for child in children:
            self.assertIn(child, parent.children)

    def test_remove_child(self):
        """Test removing a child from a node."""
        parent = Node(1)
        child = Node(2)
        parent.add_child(child)
        parent.remove_child(child)

        self.assertEqual(len(parent.children), 0)
        self.assertIsNone(child.parent)

    def test_add_duplicate_child_raises_error(self):
        """Test that adding the same child twice raises an error."""
        parent = Node(1)
        child = Node(2)
        parent.add_child(child)

        with self.assertRaises(ValueError):
            parent.add_child(child)

    def test_add_non_node_child_raises_error(self):
        """Test that adding non-Node objects raises an error."""
        parent = Node(1)

        with self.assertRaises(TypeError):
            parent.add_child(42)

    def test_remove_non_existent_child_raises_error(self):
        """Test that removing a child that doesn't exist raises an error."""
        parent = Node(1)
        child = Node(2)

        with self.assertRaises(ValueError):
            parent.remove_child(child)

    def test_node_repr(self):
        """Test the string representation of a node."""
        node = Node(42)
        repr_str = repr(node)
        self.assertIn("42", repr_str)
        self.assertIn("Node", repr_str)

    def test_node_equality(self):
        """Test node equality (based on identity, not value)."""
        node1 = Node(42)
        node2 = Node(42)
        node3 = node1

        self.assertEqual(node1, node3)
        self.assertNotEqual(node1, node2)

    def test_invalid_parent_type_raises_error(self):
        """Test that invalid parent type raises an error."""
        with self.assertRaises(TypeError):
            Node(1, parent=42)


class TestRecursiveTraversal(unittest.TestCase):
    """Test cases for the recursive traversal algorithm."""

    def setUp(self):
        """Set up traversal algorithm for testing."""
        self.traversal = ReverseBackwardTraversal()

    def test_single_node(self):
        """Test traversal of a single node."""
        root = Node(1)
        result = self.traversal.traverse_recursive(root)
        self.assertEqual(result, [1])

    def test_empty_tree(self):
        """Test traversal of an empty tree (None)."""
        result = self.traversal.traverse_recursive(None)
        self.assertEqual(result, [])

    def test_simple_tree(self):
        """Test traversal of a simple three-node tree."""
        root = Node(1)
        left = Node(2)
        right = Node(3)
        root.add_child(left)
        root.add_child(right)

        result = self.traversal.traverse_recursive(root)
        # Post-order: visit children before parent
        self.assertEqual(result, [2, 3, 1])

    def test_example_tree(self):
        """Test traversal of the example tree."""
        root = build_example_tree()
        result = self.traversal.traverse_recursive(root)
        # Expected post-order: [4, 5, 2, 6, 3, 1]
        self.assertEqual(result, [4, 5, 2, 6, 3, 1])

    def test_deep_tree(self):
        """Test traversal of a deep tree."""
        # Create a linear tree: 1 -> 2 -> 3 -> 4 -> 5
        root = Node(1)
        current = root
        for i in range(2, 6):
            child = Node(i)
            current.add_child(child)
            current = child

        result = self.traversal.traverse_recursive(root)
        # Post-order: deepest first
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_invalid_root_type_raises_error(self):
        """Test that invalid root type raises an error."""
        with self.assertRaises(TypeError):
            self.traversal.traverse_recursive(42)

    def test_wide_tree(self):
        """Test traversal of a wide tree (many children)."""
        root = Node(1)
        for i in range(2, 7):
            root.add_child(Node(i))

        result = self.traversal.traverse_recursive(root)
        # Post-order: all children, then parent
        expected = [2, 3, 4, 5, 6, 1]
        self.assertEqual(result, expected)


class TestIterativeTraversal(unittest.TestCase):
    """Test cases for the iterative traversal algorithm."""

    def setUp(self):
        """Set up traversal algorithm for testing."""
        self.traversal = ReverseBackwardTraversal()

    def test_single_node(self):
        """Test iterative traversal of a single node."""
        root = Node(1)
        result = self.traversal.traverse_iterative(root)
        self.assertEqual(result, [1])

    def test_empty_tree(self):
        """Test iterative traversal of an empty tree."""
        result = self.traversal.traverse_iterative(None)
        self.assertEqual(result, [])

    def test_simple_tree(self):
        """Test iterative traversal of a simple tree."""
        root = Node(1)
        left = Node(2)
        right = Node(3)
        root.add_child(left)
        root.add_child(right)

        result = self.traversal.traverse_iterative(root)
        self.assertEqual(result, [2, 3, 1])

    def test_example_tree(self):
        """Test iterative traversal of the example tree."""
        root = build_example_tree()
        result = self.traversal.traverse_iterative(root)
        self.assertEqual(result, [4, 5, 2, 6, 3, 1])

    def test_matches_recursive(self):
        """Test that iterative and recursive produce same results."""
        root = build_example_tree()
        recursive_result = self.traversal.traverse_recursive(root)
        iterative_result = self.traversal.traverse_iterative(root)
        self.assertEqual(recursive_result, iterative_result)

    def test_invalid_root_type_raises_error(self):
        """Test that invalid root type raises an error."""
        with self.assertRaises(TypeError):
            self.traversal.traverse_iterative("invalid")


class TestCallbackTraversal(unittest.TestCase):
    """Test cases for callback-based traversal."""

    def setUp(self):
        """Set up traversal algorithm for testing."""
        self.traversal = ReverseBackwardTraversal()

    def test_callback_execution(self):
        """Test that callback is executed for each node."""
        root = Node(1)
        root.add_child(Node(2))
        root.add_child(Node(3))

        collected = []
        self.traversal.traverse_with_callback(
            root, lambda x: collected.append(x)
        )

        self.assertEqual(collected, [2, 3, 1])

    def test_callback_with_iterative_method(self):
        """Test callback with iterative method."""
        root = build_example_tree()
        collected = []

        self.traversal.traverse_with_callback(
            root, lambda x: collected.append(x), method='iterative'
        )

        self.assertEqual(collected, [4, 5, 2, 6, 3, 1])

    def test_invalid_callback_raises_error(self):
        """Test that non-callable callback raises an error."""
        root = Node(1)

        with self.assertRaises(TypeError):
            self.traversal.traverse_with_callback(root, "not_callable")

    def test_invalid_method_raises_error(self):
        """Test that invalid method name raises an error."""
        root = Node(1)

        with self.assertRaises(ValueError):
            self.traversal.traverse_with_callback(
                root, lambda x: None, method='invalid'
            )

    def test_callback_with_empty_tree(self):
        """Test callback with empty tree."""
        collected = []
        self.traversal.traverse_with_callback(
            None, lambda x: collected.append(x)
        )
        self.assertEqual(collected, [])


class TestDepthLevelTraversal(unittest.TestCase):
    """Test cases for depth-level traversal."""

    def setUp(self):
        """Set up traversal algorithm for testing."""
        self.traversal = ReverseBackwardTraversal()

    def test_single_node_depth(self):
        """Test depth traversal of a single node."""
        root = Node(1)
        result = self.traversal.traverse_by_depth(root)
        self.assertEqual(result, [[1]])

    def test_empty_tree_depth(self):
        """Test depth traversal of an empty tree."""
        result = self.traversal.traverse_by_depth(None)
        self.assertEqual(result, [])

    def test_simple_tree_depth(self):
        """Test depth traversal of a simple tree."""
        root = Node(1)
        left = Node(2)
        right = Node(3)
        root.add_child(left)
        root.add_child(right)

        result = self.traversal.traverse_by_depth(root)
        # Grouped by depth, bottom-up: [[2, 3], [1]]
        self.assertEqual(result, [[2, 3], [1]])

    def test_example_tree_depth(self):
        """Test depth traversal of the example tree."""
        root = build_example_tree()
        result = self.traversal.traverse_by_depth(root)
        # Tree structure: root=1, children=[2,3], grandchildren=[4,5,6]
        # Bottom-up: [[4, 5, 6], [2, 3], [1]]
        self.assertEqual(result, [[4, 5, 6], [2, 3], [1]])

    def test_invalid_root_type_raises_error(self):
        """Test that invalid root type raises an error."""
        with self.assertRaises(TypeError):
            self.traversal.traverse_by_depth(123)


class TestComplexScenarios(unittest.TestCase):
    """Test cases for complex real-world scenarios."""

    def setUp(self):
        """Set up traversal algorithm for testing."""
        self.traversal = ReverseBackwardTraversal()

    def test_unbalanced_tree(self):
        """Test traversal of an unbalanced tree."""
        root = Node(1)
        # Left-heavy tree
        current = root
        for i in range(2, 5):
            child = Node(i)
            current.add_child(child)
            current = child

        right = Node(5)
        root.add_child(right)

        result = self.traversal.traverse_recursive(root)
        # Post-order traversal
        self.assertEqual(result, [4, 3, 2, 5, 1])

    def test_complex_tree_structure(self):
        """Test a more complex tree structure."""
        root = Node('A')
        b = Node('B')
        c = Node('C')
        d = Node('D')
        e = Node('E')
        f = Node('F')

        root.add_child(b)
        root.add_child(c)
        b.add_child(d)
        b.add_child(e)
        c.add_child(f)

        result = self.traversal.traverse_recursive(root)
        expected = ['D', 'E', 'B', 'F', 'C', 'A']
        self.assertEqual(result, expected)

    def test_all_methods_consistent(self):
        """Test that all traversal methods produce consistent results."""
        root = build_example_tree()

        recursive = self.traversal.traverse_recursive(root)
        iterative = self.traversal.traverse_iterative(root)

        # Collect via callback
        callback_result = []
        self.traversal.traverse_with_callback(
            root, lambda x: callback_result.append(x)
        )

        # All should be equal
        self.assertEqual(recursive, iterative)
        self.assertEqual(iterative, callback_result)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def setUp(self):
        """Set up traversal algorithm for testing."""
        self.traversal = ReverseBackwardTraversal()

    def test_very_deep_tree(self):
        """Test traversal of a very deep tree (checks recursion depth)."""
        root = Node(0)
        current = root
        depth = 100

        for i in range(1, depth):
            child = Node(i)
            current.add_child(child)
            current = child

        # Iterative should handle this without recursion limit issues
        result = self.traversal.traverse_iterative(root)
        self.assertEqual(len(result), depth)
        self.assertEqual(result[-1], 0)  # Root is last

    def test_none_values_in_nodes(self):
        """Test nodes with None as their value."""
        root = Node(None)
        child = Node(None)
        root.add_child(child)

        result = self.traversal.traverse_recursive(root)
        self.assertEqual(result, [None, None])

    def test_mixed_type_values(self):
        """Test nodes with mixed value types."""
        root = Node(1)
        root.add_child(Node("string"))
        root.add_child(Node(3.14))
        root.add_child(Node([1, 2, 3]))
        root.add_child(Node({'key': 'value'}))

        result = self.traversal.traverse_recursive(root)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[-1], 1)  # Root is last


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestNodeClass))
    suite.addTests(loader.loadTestsFromTestCase(TestRecursiveTraversal))
    suite.addTests(loader.loadTestsFromTestCase(TestIterativeTraversal))
    suite.addTests(loader.loadTestsFromTestCase(TestCallbackTraversal))
    suite.addTests(loader.loadTestsFromTestCase(TestDepthLevelTraversal))
    suite.addTests(loader.loadTestsFromTestCase(TestComplexScenarios))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
