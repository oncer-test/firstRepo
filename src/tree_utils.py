from typing import Optional

class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value stored in the node.
        left (Optional[TreeNode]): Reference to the left child node.
        right (Optional[TreeNode]): Reference to the right child node.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """
        Initialize a new TreeNode.

        Args:
            val (int, optional): Value of the node. Defaults to 0.
            left (Optional[TreeNode], optional): Left child node. Defaults to None.
            right (Optional[TreeNode], optional): Right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


def mirror_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Mirror a binary tree by recursively swapping left and right children.

    Reverses the structure of the tree in-place, maintaining node values.
    Each node's left and right children are swapped recursively.

    Args:
        root (Optional[TreeNode]): Root node of the binary tree to mirror.

    Returns:
        Optional[TreeNode]: Root of the mirrored tree.

    Time Complexity: O(n), where n is the number of nodes
    Space Complexity: O(h), where h is the height of the tree (recursive call stack)

    Example:
        Input:     1            Output:    1
                  / \                    / \
                 2   3                  3   2
    """
    def _mirror_subtree(node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Helper function to mirror a subtree.
        First mirrors the children, then swaps them.
        """
        # Base case: if node is None, return None
        if node is None:
            return None

        # Store original children
        orig_left = node.left
        orig_right = node.right

        # Recursively mirror children subtrees first
        # Crucially, mirror with the OPPOSITE subtree
        node.left = _mirror_subtree(orig_right)
        node.right = _mirror_subtree(orig_left)

        return node

    return _mirror_subtree(root)