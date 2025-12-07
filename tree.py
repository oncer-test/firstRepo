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
        # BFS: top-to-bottom, left-to-right per level using deque
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result

    def level_order_traversal_right_to_left(self):
        # BFS: top-to-bottom, right-to-left per level (level reversed)
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes[::-1])

        return result

    def reverse_level_order_traversal(self):
        # BFS: bottom-to-top, left-to-right per level (levels reversed)
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result[::-1]

    def reverse_inorder_traversal(self):
        # DFS: Right -> Node -> Left (reverse in-order)
        result = []
        self._reverse_inorder_helper(self.root, result)
        return result

    def _reverse_inorder_helper(self, node, result):
        if node is None:
            return
        self._reverse_inorder_helper(node.right, result)
        result.append(node.value)
        self._reverse_inorder_helper(node.left, result)

    def reverse_preorder_traversal(self):
        # DFS: Node -> Right -> Left (reverse pre-order)
        result = []
        self._reverse_preorder_helper(self.root, result)
        return result

    def _reverse_preorder_helper(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._reverse_preorder_helper(node.right, result)
        self._reverse_preorder_helper(node.left, result)

    def reverse_postorder_traversal(self):
        # DFS: Right -> Left -> Node (reverse post-order)
        result = []
        self._reverse_postorder_helper(self.root, result)
        return result

    def _reverse_postorder_helper(self, node, result):
        if node is None:
            return
        self._reverse_postorder_helper(node.right, result)
        self._reverse_postorder_helper(node.left, result)
        result.append(node.value)

    def POST_RUN_SUMMARY_level_order_traversal_left_to_right(self):
        return "level_order_traversal_left_to_right: BFS approach, O(n) time, processes levels left-to-right"

    def reverse_level_order_traversal_right_to_left(self):
        # BFS: bottom-to-top, right-to-left per level (both dimensions reversed)
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return [level[::-1] for level in result[::-1]]

    def reverse_even_levels(self):
        # BFS: top-to-bottom with alternating level reversal (even indices reversed)
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return [level[::-1] if i % 2 == 0 else level for i, level in enumerate(result)]

    def POST_RUN_SUMMARY(self):
        # Summary of BinaryTree class traversal methods
        return {
            "class": "BinaryTree",
            "methods_count": 9,
            "traversal_types": ["level-order", "depth-first"],
            "directions": ["left-to-right", "right-to-left", "top-to-bottom", "bottom-to-top", "alternating"],
            "time_complexity": "O(n)",
            "space_complexity": "O(w) or O(h)"
        }

    def POST_RUN_SUMMARY_level_order_traversal_left_to_right(self):
        return {
            "method": "level_order_traversal_left_to_right",
            "approach": "BFS with deque",
            "time_complexity": "O(n)",
            "space_complexity": "O(w)"
        }
