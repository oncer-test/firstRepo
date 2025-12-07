import unittest
from tree import TreeNode, BinaryTree


class TestTreeNode(unittest.TestCase):
    # Tests for TreeNode class basic functionality

    def test_node_creation(self):
        # Verify TreeNode can be created with value only
        node = TreeNode(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_node_with_children(self):
        # Verify TreeNode can be created with left and right children
        left_child = TreeNode(3)
        right_child = TreeNode(7)
        parent = TreeNode(5, left_child, right_child)

        self.assertEqual(parent.value, 5)
        self.assertEqual(parent.left.value, 3)
        self.assertEqual(parent.right.value, 7)

    def test_node_repr(self):
        # Verify TreeNode string representation
        node = TreeNode(42)
        self.assertEqual(repr(node), "TreeNode(42)")


class TestBinaryTreeReverseLevelOrder(unittest.TestCase):
    # Tests for reverse level-order traversal (left-to-right, reversed levels)

    def test_empty_tree(self):
        # Verify empty tree returns empty list
        tree = BinaryTree()
        result = tree.reverse_level_order_traversal()
        self.assertEqual(result, [])

    def test_single_node(self):
        # Verify single-node tree returns one level
        root = TreeNode(1)
        tree = BinaryTree(root)
        result = tree.reverse_level_order_traversal()
        self.assertEqual(result, [[1]])

    def test_three_node_tree(self):
        # Verify three-node tree: root with left and right children
        #     1
        #    / \
        #   2   3
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        tree = BinaryTree(root)
        result = tree.reverse_level_order_traversal()
        # Levels are: [[1], [2, 3]], reversed to [[2, 3], [1]]
        self.assertEqual(result, [[2, 3], [1]])

    def test_full_binary_tree(self):
        # Verify full binary tree with 4 levels
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
        result = tree.reverse_level_order_traversal()
        # Levels: [[1], [2, 3], [4, 5, 6, 7]], reversed
        expected = [[4, 5, 6, 7], [2, 3], [1]]
        self.assertEqual(result, expected)

    def test_unbalanced_tree_left_heavy(self):
        # Verify unbalanced tree with more left nodes
        #     1
        #    /
        #   2
        #  / \
        # 3   4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)

        tree = BinaryTree(root)
        result = tree.reverse_level_order_traversal()
        # Levels: [[1], [2], [3, 4]], reversed
        expected = [[3, 4], [2], [1]]
        self.assertEqual(result, expected)

    def test_unbalanced_tree_right_heavy(self):
        # Verify unbalanced tree with more right nodes
        #   1
        #    \
        #     2
        #    / \
        #   3   4
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)

        tree = BinaryTree(root)
        result = tree.reverse_level_order_traversal()
        # Levels: [[1], [2], [3, 4]], reversed
        expected = [[3, 4], [2], [1]]
        self.assertEqual(result, expected)


class TestBinaryTreeReverseInorder(unittest.TestCase):
    # Tests for reverse in-order traversal (right -> node -> left)

    def test_empty_tree(self):
        # Verify empty tree returns empty list
        tree = BinaryTree()
        result = tree.reverse_inorder_traversal()
        self.assertEqual(result, [])

    def test_single_node(self):
        # Verify single-node tree returns just the node value
        root = TreeNode(1)
        tree = BinaryTree(root)
        result = tree.reverse_inorder_traversal()
        self.assertEqual(result, [1])

    def test_three_node_tree(self):
        # Verify three-node tree reverse in-order traversal
        #   1
        #  / \
        # 2   3
        # Reverse in-order: right(3) -> node(1) -> left(2)
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        tree = BinaryTree(root)
        result = tree.reverse_inorder_traversal()
        self.assertEqual(result, [3, 1, 2])

    def test_full_binary_tree(self):
        # Verify full binary tree reverse in-order
        #      1
        #     / \
        #    2   3
        #   / \ / \
        #  4  5 6  7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        tree = BinaryTree(root)
        result = tree.reverse_inorder_traversal()
        # Right -> Node -> Left at each level: 7->3->6->1->5->2->4
        expected = [7, 3, 6, 1, 5, 2, 4]
        self.assertEqual(result, expected)

    def test_left_skewed_tree(self):
        # Verify left-skewed tree (only left children)
        # 1
        # /
        # 2
        # /
        # 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        tree = BinaryTree(root)
        result = tree.reverse_inorder_traversal()
        # No right subtrees: 1 -> 2 -> 3
        self.assertEqual(result, [1, 2, 3])

    def test_right_skewed_tree(self):
        # Verify right-skewed tree (only right children)
        #   1
        #    \
        #     2
        #      \
        #       3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        tree = BinaryTree(root)
        result = tree.reverse_inorder_traversal()
        # Only right subtrees: 3 -> 2 -> 1
        self.assertEqual(result, [3, 2, 1])


class TestBinaryTreeReversePreorder(unittest.TestCase):
    # Tests for reverse pre-order traversal (node -> right -> left)

    def test_empty_tree(self):
        # Verify empty tree returns empty list
        tree = BinaryTree()
        result = tree.reverse_preorder_traversal()
        self.assertEqual(result, [])

    def test_single_node(self):
        # Verify single-node tree returns just the node value
        root = TreeNode(1)
        tree = BinaryTree(root)
        result = tree.reverse_preorder_traversal()
        self.assertEqual(result, [1])

    def test_three_node_tree(self):
        # Verify three-node tree reverse pre-order traversal
        #   1
        #  / \
        # 2   3
        # Reverse pre-order: node(1) -> right(3) -> left(2)
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        tree = BinaryTree(root)
        result = tree.reverse_preorder_traversal()
        self.assertEqual(result, [1, 3, 2])

    def test_full_binary_tree(self):
        # Verify full binary tree reverse pre-order
        #      1
        #     / \
        #    2   3
        #   / \ / \
        #  4  5 6  7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        tree = BinaryTree(root)
        result = tree.reverse_preorder_traversal()
        # Node -> Right -> Left: 1->3->7->6->2->5->4
        expected = [1, 3, 7, 6, 2, 5, 4]
        self.assertEqual(result, expected)


class TestBinaryTreeReversePostorder(unittest.TestCase):
    # Tests for reverse post-order traversal (right -> left -> node)

    def test_empty_tree(self):
        # Verify empty tree returns empty list
        tree = BinaryTree()
        result = tree.reverse_postorder_traversal()
        self.assertEqual(result, [])

    def test_single_node(self):
        # Verify single-node tree returns just the node value
        root = TreeNode(1)
        tree = BinaryTree(root)
        result = tree.reverse_postorder_traversal()
        self.assertEqual(result, [1])

    def test_three_node_tree(self):
        # Verify three-node tree reverse post-order traversal
        #   1
        #  / \
        # 2   3
        # Reverse post-order: right(3) -> left(2) -> node(1)
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        tree = BinaryTree(root)
        result = tree.reverse_postorder_traversal()
        self.assertEqual(result, [3, 2, 1])

    def test_full_binary_tree(self):
        # Verify full binary tree reverse post-order
        #      1
        #     / \
        #    2   3
        #   / \ / \
        #  4  5 6  7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        tree = BinaryTree(root)
        result = tree.reverse_postorder_traversal()
        # Right -> Left -> Node: 7->6->3->5->4->2->1
        expected = [7, 6, 3, 5, 4, 2, 1]
        self.assertEqual(result, expected)


class TestBinaryTreeReverseEvenLevels(unittest.TestCase):
    # Tests for reverse even levels traversal - reverses only even-indexed levels (0, 2, 4, ...)

    def test_empty_tree(self):
        # Verify empty tree returns empty list
        tree = BinaryTree()
        result = tree.reverse_even_levels()
        self.assertEqual(result, [])

    def test_single_node(self):
        # Verify single-node tree - level 0 is even, but single element remains same
        root = TreeNode(1)
        tree = BinaryTree(root)
        result = tree.reverse_even_levels()
        self.assertEqual(result, [[1]])

    def test_two_level_tree(self):
        # Verify two-level tree with even and odd level reversal
        #     1
        #    / \
        #   2   3
        # Level 0 (even): [1] reversed = [1] (single element)
        # Level 1 (odd):  [2, 3] unchanged = [2, 3]
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        tree = BinaryTree(root)
        result = tree.reverse_even_levels()
        expected = [[1], [2, 3]]
        self.assertEqual(result, expected)

    def test_three_level_full_binary_tree(self):
        # Verify three-level full binary tree with alternating reversal
        #        1
        #       / \
        #      2   3
        #     / \ / \
        #    4  5 6  7
        # Level 0 (even): [1] reversed = [1]
        # Level 1 (odd):  [2, 3] unchanged = [2, 3]
        # Level 2 (even): [4, 5, 6, 7] reversed = [7, 6, 5, 4]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        tree = BinaryTree(root)
        result = tree.reverse_even_levels()
        expected = [[1], [2, 3], [7, 6, 5, 4]]
        self.assertEqual(result, expected)

    def test_four_level_tree(self):
        # Verify four-level tree with alternating even/odd reversal
        #          1
        #        /   \
        #       2     3
        #      / \   / \
        #     4   5 6   7
        #    /
        #   8
        # Level 0 (even): [1] reversed = [1]
        # Level 1 (odd):  [2, 3] unchanged = [2, 3]
        # Level 2 (even): [4, 5, 6, 7] reversed = [7, 6, 5, 4]
        # Level 3 (odd):  [8] unchanged = [8]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)

        tree = BinaryTree(root)
        result = tree.reverse_even_levels()
        expected = [[1], [2, 3], [7, 6, 5, 4], [8]]
        self.assertEqual(result, expected)

    def test_unbalanced_left_heavy_tree(self):
        # Verify unbalanced left-heavy tree
        #     1
        #    /
        #   2
        #  / \
        # 3   4
        # Level 0 (even): [1] reversed = [1]
        # Level 1 (odd):  [2] unchanged = [2]
        # Level 2 (even): [3, 4] reversed = [4, 3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)

        tree = BinaryTree(root)
        result = tree.reverse_even_levels()
        expected = [[1], [2], [4, 3]]
        self.assertEqual(result, expected)

    def test_unbalanced_right_heavy_tree(self):
        # Verify unbalanced right-heavy tree
        #   1
        #    \
        #     2
        #    / \
        #   3   4
        # Level 0 (even): [1] reversed = [1]
        # Level 1 (odd):  [2] unchanged = [2]
        # Level 2 (even): [3, 4] reversed = [4, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)

        tree = BinaryTree(root)
        result = tree.reverse_even_levels()
        expected = [[1], [2], [4, 3]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
