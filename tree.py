from collections import deque


class TreeNode:
    # Represents a single node in a binary tree
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.value})"


class BinaryTree:
    # Manages a binary tree structure and provides traversal operations
    def __init__(self, root=None):
        self.root = root

    def reverse_level_order_traversal(self):
        # Traverses tree level by level from left to right, but returns levels in reverse order
        # Uses BFS approach with a deque to collect levels, then reverses
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level (left to right)
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        # Reverse the order of levels
        return result[::-1]

    def reverse_inorder_traversal(self):
        # Performs in-order traversal in reverse (right subtree -> node -> left subtree)
        # Uses recursive DFS approach
        result = []
        self._reverse_inorder_helper(self.root, result)
        return result

    def _reverse_inorder_helper(self, node, result):
        # Helper method for reverse in-order traversal
        # Visits right subtree first, then node, then left subtree
        if node is None:
            return

        # Process right subtree first (for reverse order)
        self._reverse_inorder_helper(node.right, result)

        # Process current node
        result.append(node.value)

        # Process left subtree
        self._reverse_inorder_helper(node.left, result)

    def reverse_preorder_traversal(self):
        # Performs pre-order traversal in reverse (node -> right subtree -> left subtree)
        # Uses recursive DFS approach
        result = []
        self._reverse_preorder_helper(self.root, result)
        return result

    def _reverse_preorder_helper(self, node, result):
        # Helper method for reverse pre-order traversal
        # Processes node first, then right subtree, then left subtree
        if node is None:
            return

        # Process current node first
        result.append(node.value)

        # Process right subtree before left (for reverse order)
        self._reverse_preorder_helper(node.right, result)

        # Process left subtree
        self._reverse_preorder_helper(node.left, result)

    def reverse_postorder_traversal(self):
        # Performs post-order traversal in reverse (right subtree -> left subtree -> node)
        # Uses recursive DFS approach
        result = []
        self._reverse_postorder_helper(self.root, result)
        return result

    def _reverse_postorder_helper(self, node, result):
        # Helper method for reverse post-order traversal
        # Processes right subtree first, then left subtree, then node
        if node is None:
            return

        # Process right subtree first
        self._reverse_postorder_helper(node.right, result)

        # Process left subtree
        self._reverse_postorder_helper(node.left, result)

        # Process current node last
        result.append(node.value)
