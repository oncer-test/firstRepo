from collections import deque


class TreeNode:
    # Represents a single node in a binary tree
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.value})"


class BackwardsTree:
    # Manages a binary tree structure with focus on right-to-left traversal operations
    # This class specializes in traversing trees from right to left direction
    def __init__(self, root=None):
        self.root = root

    def level_order_traversal_right_to_left(self):
        # Traverses tree level by level from top to bottom, with each level ordered right to left
        # Uses BFS approach with a deque to collect levels in forward order, then reverses each level
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

                # Add children to queue for next level (add right before left for natural right-to-left order)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            # Each level is naturally processed right-to-left due to child order
            result.append(level_nodes)

        return result

    def reverse_level_order_traversal_right_to_left(self):
        # Traverses tree level by level from bottom to top, with each level ordered right to left
        # Uses BFS approach to collect all levels, then reverses both level order and node order
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level (right to left)
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                # Add children to queue in reverse order (right before left)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            result.append(level_nodes)

        # Reverse levels (bottom to top) to get reverse level order
        return result[::-1]

    def reverse_inorder_traversal_right_to_left(self):
        # Performs in-order traversal starting from right (right subtree -> node -> left subtree)
        # This is the natural reverse of standard in-order traversal
        # Uses recursive DFS approach
        result = []
        self._reverse_inorder_helper(self.root, result)
        return result

    def _reverse_inorder_helper(self, node, result):
        # Helper method for reverse in-order traversal (right-to-left bias)
        # Visits right subtree first, then node, then left subtree
        if node is None:
            return

        # Process right subtree first (natural right-to-left direction)
        self._reverse_inorder_helper(node.right, result)

        # Process current node
        result.append(node.value)

        # Process left subtree
        self._reverse_inorder_helper(node.left, result)

    def reverse_preorder_traversal_right_to_left(self):
        # Performs pre-order traversal in reverse (node -> right subtree -> left subtree)
        # Visits node first, then explores right subtree before left subtree
        # Uses recursive DFS approach
        result = []
        self._reverse_preorder_helper(self.root, result)
        return result

    def _reverse_preorder_helper(self, node, result):
        # Helper method for reverse pre-order traversal (right-to-left bias)
        # Processes node first, then right subtree, then left subtree
        if node is None:
            return

        # Process current node first
        result.append(node.value)

        # Process right subtree before left (right-to-left direction)
        self._reverse_preorder_helper(node.right, result)

        # Process left subtree
        self._reverse_preorder_helper(node.left, result)

    def reverse_postorder_traversal_right_to_left(self):
        # Performs post-order traversal in reverse (right subtree -> left subtree -> node)
        # Visits children before parent, but right subtree before left subtree
        # Uses recursive DFS approach
        result = []
        self._reverse_postorder_helper(self.root, result)
        return result

    def _reverse_postorder_helper(self, node, result):
        # Helper method for reverse post-order traversal (right-to-left bias)
        # Processes right subtree first, then left subtree, then node
        if node is None:
            return

        # Process right subtree first (right-to-left direction)
        self._reverse_postorder_helper(node.right, result)

        # Process left subtree
        self._reverse_postorder_helper(node.left, result)

        # Process current node last
        result.append(node.value)

    def zigzag_level_order_traversal(self):
        # Traverses tree in zigzag pattern: left-to-right on even levels, right-to-left on odd levels
        # Uses BFS approach with level tracking to determine direction
        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        level = 0

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse level nodes if at odd level (right-to-left)
            if level % 2 == 1:
                level_nodes.reverse()

            result.append(level_nodes)
            level += 1

        return result

    def POST_RUN_SUMMARY_backwards_tree(self):
        # Summary of the backwards tree (right-to-left) traversal algorithms
        # This class specializes in right-to-left tree traversal operations
        #
        # Key Algorithms Implemented:
        # 1. level_order_traversal_right_to_left: BFS with right-to-left level ordering
        # 2. reverse_level_order_traversal_right_to_left: Bottom-to-top with right-to-left levels
        # 3. reverse_inorder_traversal_right_to_left: DFS (right -> node -> left)
        # 4. reverse_preorder_traversal_right_to_left: DFS (node -> right -> left)
        # 5. reverse_postorder_traversal_right_to_left: DFS (right -> left -> node)
        # 6. zigzag_level_order_traversal: Alternating left-to-right and right-to-left levels
        #
        # All algorithms process trees from right-to-left perspective:
        # - Right children are explored before left children
        # - Levels are ordered with rightmost nodes first
        # - Suitable for applications requiring reverse traversal order
        #
        # Time Complexity: O(n) for all methods where n is number of nodes
        # Space Complexity: O(w) for BFS methods, O(h) for DFS where w=width, h=height
        #
        # Example Tree Structure:
        #       1
        #      / \
        #     2   3
        #    / \ / \
        #   4  5 6  7
        #
        # Level Order (Right-to-Left): [[1], [3, 2], [7, 6, 5, 4]]
        # Reverse Level Order (Right-to-Left): [[7, 6, 5, 4], [3, 2], [1]]
        # Zigzag: [[1], [3, 2], [4, 5, 6, 7]]
        return {
            "class": "BackwardsTree",
            "focus": "Right-to-left tree traversal",
            "approach": "BFS and DFS with right-bias",
            "time_complexity": "O(n)",
            "space_complexity": "O(w) or O(h)",
            "primary_use": "Reverse-order tree processing and right-to-left exploration"
        }
