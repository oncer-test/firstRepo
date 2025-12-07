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
    # Binary tree with right-to-left traversal focus
    def __init__(self, root=None):
        self.root = root

    def level_order_traversal_right_to_left(self):
        # BFS: top-to-bottom, right-to-left per level (right child enqueued first)
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

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            result.append(level_nodes)

        return result

    def reverse_level_order_traversal_right_to_left(self):
        # BFS: bottom-to-top, right-to-left per level (levels reversed)
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

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            result.append(level_nodes)

        return result[::-1]

    def reverse_inorder_traversal_right_to_left(self):
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

    def reverse_preorder_traversal_right_to_left(self):
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

    def reverse_postorder_traversal_right_to_left(self):
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

    def zigzag_level_order_traversal(self):
        # BFS: alternating left-to-right (even levels) and right-to-left (odd levels)
        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        level = 0

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

            if level % 2 == 1:
                level_nodes.reverse()

            result.append(level_nodes)
            level += 1

        return result

    def POST_RUN_SUMMARY(self):
        # Summary of BackwardsTree class traversal methods
        return {
            "class": "BackwardsTree",
            "methods_count": 6,
            "traversal_types": ["level-order", "depth-first", "zigzag"],
            "primary_directions": ["right-to-left", "bottom-to-top", "alternating"],
            "time_complexity": "O(n)",
            "space_complexity": "O(w) or O(h)"
        }

    def POST_RUN_SUMMARY_backwards_tree(self):
        return {
            "class": "BackwardsTree",
            "focus": "Right-to-left tree traversal",
            "approach": "BFS and DFS with right-bias",
            "time_complexity": "O(n)",
            "space_complexity": "O(w) or O(h)"
        }
