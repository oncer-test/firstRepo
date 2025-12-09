import pytest
from src.tree_utils import TreeNode, mirror_tree

def print_tree(root, prefix='', is_left=True):
    """Helper function to print a tree's structure."""
    if root is None:
        print(prefix + ('└── ' if is_left else '┌── ') + 'None')
        return

    print(prefix + ('└── ' if is_left else '┌── ') + str(root.val))

    new_prefix = prefix + ('    ' if is_left else '│   ')
    print_tree(root.left, new_prefix, True)
    print_tree(root.right, new_prefix, False)

class TestTreeMirror:
    """
    Test suite for tree mirroring functionality.

    Covers various scenarios to ensure correct tree mirroring:
    - Empty tree
    - Single node tree
    - Symmetric tree
    - Asymmetric tree
    - Deep tree with multiple levels
    """

    def test_mirror_empty_tree(self):
        """
        Test mirroring an empty tree.
        Ensures that None is returned for None input.
        """
        assert mirror_tree(None) is None

    def test_mirror_single_node(self):
        """
        Test mirroring a single node tree.
        Ensures that a single node remains unchanged.
        """
        root = TreeNode(1)
        mirrored = mirror_tree(root)

        assert mirrored.val == 1
        assert mirrored.left is None
        assert mirrored.right is None

    def test_mirror_symmetric_tree(self):
        """
        Test mirroring a perfectly symmetric tree.
        Ensures that left and right children are swapped.
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        mirrored = mirror_tree(root)

        assert mirrored.val == 1
        assert mirrored.left.val == 3
        assert mirrored.right.val == 2

    def test_mirror_asymmetric_tree(self):
        """
        Test mirroring an asymmetric tree with uneven subtrees.
        Ensures that all levels of the tree are correctly mirrored.
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)

        print("Original Tree:")
        print_tree(root)

        mirrored = mirror_tree(root)

        print("\nMirrored Tree:")
        print_tree(mirrored)

        assert mirrored.val == 1
        assert mirrored.left.val == 3
        assert mirrored.right.val == 2

        # Verify the values in the tree as a set
        tree_vals = set()

        def collect_tree_vals(node):
            if node is None:
                return

            tree_vals.add(node.val)
            collect_tree_vals(node.left)
            collect_tree_vals(node.right)

        collect_tree_vals(mirrored)
        assert tree_vals == {1, 2, 3, 4, 5}

    def test_mirror_deep_tree(self):
        """
        Test mirroring a deep, complex tree.
        Ensures that multiple levels are correctly mirrored.
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        mirrored = mirror_tree(root)

        assert mirrored.val == 1
        assert mirrored.left.val == 3
        assert mirrored.right.val == 2
        assert mirrored.left.left.val == 7
        assert mirrored.left.right.val == 6
        assert mirrored.right.left.val == 5
        assert mirrored.right.right.val == 4