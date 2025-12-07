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


if __name__ == '__main__':
    unittest.main()
