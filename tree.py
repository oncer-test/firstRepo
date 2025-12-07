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

    def level_order_traversal_left_to_right(self):
        # Traverses tree level by level from left to right (top to bottom)
        # Uses BFS approach with a deque to collect levels in forward order
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

        return result

    def level_order_traversal_right_to_left(self):
        # Traverses tree level by level from right to left (top to bottom)
        # Uses BFS approach with a deque to collect levels, reversing each level
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level (left to right), then reverse for right-to-left order
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the level to get right-to-left order
            result.append(level_nodes[::-1])

        return result

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

    def POST_RUN_SUMMARY_level_order_traversal_left_to_right(self):
        # Summary of the left-to-right level order traversal algorithm
        # This algorithm performs a breadth-first search (BFS) traversal of the tree
        # Processing nodes level by level from top to bottom, and within each level from left to right
        # Uses a queue (deque) to maintain nodes to be processed
        # Time complexity: O(n) where n is the number of nodes
        # Space complexity: O(w) where w is the maximum width of the tree
        # Returns a list of lists, where each inner list contains node values at that level
        # Example: For a tree with levels [1], [2,3], [4,5,6,7] returns [[1], [2,3], [4,5,6,7]]
        return "level_order_traversal_left_to_right: BFS approach, O(n) time, processes levels left-to-right"

    def reverse_level_order_traversal_right_to_left(self):
        # Traverses tree level by level from bottom to top, with each level ordered right to left
        # Uses BFS approach to collect all levels, then reverses both level order and node order within each level
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

        # Reverse levels (bottom to top) and reverse each level (right to left)
        return [level[::-1] for level in result[::-1]]

    def POST_RUN_SUMMARY_level_order_traversal_left_to_right(self):
        # Summary of the left-to-right level order traversal algorithm
        # This algorithm performs breadth-first search (BFS) traversal of the binary tree
        # Processing nodes level by level from top to bottom, with each level ordered left to right
        #
        # Algorithm Overview:
        # 1. Initialize a queue with the root node
        # 2. While queue is not empty:
        #    a. Get the current level size (number of nodes at this level)
        #    b. Process all nodes at this level by dequeuing and appending their values
        #    c. Enqueue the left child if it exists
        #    d. Enqueue the right child if it exists
        #    e. Add the level's values to result
        # 3. Return result containing all levels
        #
        # Time Complexity: O(n) where n is the number of nodes - visits each node once
        # Space Complexity: O(w) where w is the maximum width of the tree - queue holds nodes at widest level
        #
        # Use Cases:
        # - Level-by-level tree traversal
        # - Finding siblings at the same level
        # - Building tree level lists
        # - Shortest path in unweighted trees
        #
        # Example Tree:
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        # Returns: [[1], [2, 3], [4, 5]]
        return {
            "method": "level_order_traversal_left_to_right",
            "approach": "BFS with deque",
            "time_complexity": "O(n)",
            "space_complexity": "O(w)",
            "description": "Breadth-first traversal processing each level left to right"
        }
