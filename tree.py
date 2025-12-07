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
        # Breadth-First Search (BFS) traversal processing tree from top to bottom,
        # with each level ordered left to right based on child insertion order
        #
        # Algorithm:
        # 1. Initialize queue with root node
        # 2. While queue has nodes:
        #    a. Capture current queue length (nodes at this level)
        #    b. Process exactly that many nodes from queue
        #    c. For each node: extract value and enqueue its children (left then right)
        #    d. Append collected node values as a single level to result
        # 3. Return result as list of lists, one per tree level
        #
        # Key aspect: left child enqueued before right child maintains natural left-to-right order
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

                # Add children to queue for next level (left first ensures left-to-right order)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result

    def level_order_traversal_right_to_left(self):
        # Breadth-First Search (BFS) traversal with level reversal to achieve right-to-left order
        # Processes tree top-to-bottom, but displays each level with rightmost node first
        #
        # Algorithm:
        # 1. Standard BFS: initialize queue with root
        # 2. Process levels by dequeuing nodes in natural order (left-to-right arrival)
        # 3. For each level, collect node values then reverse using Python's slice notation
        # 4. Return levels in original top-to-bottom order but with nodes reversed
        #
        # Difference from level_order_traversal_left_to_right:
        # - Same traversal pattern, different output format
        # - Each level reversed individually using [::-1] slice
        # - Useful for applications requiring right-first display without changing tree structure
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level (collected left to right, displayed right to left)
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the level to get right-to-left order display
            result.append(level_nodes[::-1])

        return result

    def reverse_level_order_traversal(self):
        # Breadth-First Search with level order reversal - traversal from bottom to top
        # Maintains left-to-right ordering within each level, but returns levels bottom-to-top
        #
        # Algorithm:
        # 1. Perform standard BFS collecting all levels from root to leaves
        # 2. Collect node values in natural left-to-right order for each level
        # 3. After collecting all levels, reverse the entire result list
        # 4. Return levels in bottom-to-top sequence
        #
        # Use case: Useful for processing trees from leaf level upward without recursion
        # Note: Within each level, nodes remain left-to-right ordered
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

        # Reverse the order of levels (bottom-to-top)
        return result[::-1]

    def reverse_inorder_traversal(self):
        # Reverse in-order traversal using Depth-First Search (DFS)
        # Processes nodes: Right Subtree -> Current Node -> Left Subtree
        # This is the opposite of standard in-order (Left -> Node -> Right)
        #
        # Algorithm:
        # 1. Use recursive helper with call stack for DFS
        # 2. For each node, recursively process right subtree first
        # 3. Then append current node's value to result
        # 4. Finally recursively process left subtree
        # 5. Results in descending-like order (largest to smallest in BST)
        #
        # Complexity: O(n) time, O(h) space for recursion stack
        result = []
        self._reverse_inorder_helper(self.root, result)
        return result

    def _reverse_inorder_helper(self, node, result):
        # Recursive helper for reverse in-order traversal
        # Implements the Right -> Current -> Left processing order
        if node is None:
            return

        # Process right subtree first (gives reverse ordering effect)
        self._reverse_inorder_helper(node.right, result)

        # Process current node
        result.append(node.value)

        # Process left subtree
        self._reverse_inorder_helper(node.left, result)

    def reverse_preorder_traversal(self):
        # Reverse pre-order traversal using Depth-First Search (DFS)
        # Processes nodes: Current Node -> Right Subtree -> Left Subtree
        # This reverses standard pre-order (Node -> Left -> Right) by swapping left/right
        #
        # Algorithm:
        # 1. Recursively process in order: current node, then right, then left
        # 2. Node is processed first (pre-order characteristic)
        # 3. Right subtree processed before left (reverse characteristic)
        # 4. Useful for tree copying and hierarchical processing in reverse
        #
        # Complexity: O(n) time, O(h) space for recursion stack
        result = []
        self._reverse_preorder_helper(self.root, result)
        return result

    def _reverse_preorder_helper(self, node, result):
        # Recursive helper for reverse pre-order traversal
        # Implements Node -> Right Subtree -> Left Subtree order
        if node is None:
            return

        # Process current node first (pre-order characteristic)
        result.append(node.value)

        # Process right subtree before left (reverse characteristic)
        self._reverse_preorder_helper(node.right, result)

        # Process left subtree
        self._reverse_preorder_helper(node.left, result)

    def reverse_postorder_traversal(self):
        # Reverse post-order traversal using Depth-First Search (DFS)
        # Processes nodes: Right Subtree -> Left Subtree -> Current Node
        # This reverses standard post-order (Left -> Right -> Node) by swapping subtrees
        #
        # Algorithm:
        # 1. Recursively process: right subtree, then left subtree, then node
        # 2. Node is processed last (post-order characteristic)
        # 3. Right subtree processed before left (reverse characteristic)
        # 4. Useful for cleanup operations in reverse (delete right, then left, then root)
        #
        # Complexity: O(n) time, O(h) space for recursion stack
        result = []
        self._reverse_postorder_helper(self.root, result)
        return result

    def _reverse_postorder_helper(self, node, result):
        # Recursive helper for reverse post-order traversal
        # Implements Right Subtree -> Left Subtree -> Node order
        if node is None:
            return

        # Process right subtree first (reverse characteristic)
        self._reverse_postorder_helper(node.right, result)

        # Process left subtree
        self._reverse_postorder_helper(node.left, result)

        # Process current node last (post-order characteristic)
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
        # Combined level order and node order reversal - bottom-to-top, right-to-left
        # Performs standard BFS then applies two reversals:
        # 1. Reverses the entire level list (bottom-to-top)
        # 2. Reverses each individual level (right-to-left)
        #
        # Algorithm:
        # 1. Standard BFS collection from root to leaves
        # 2. After collecting all levels, apply list comprehension to reverse both:
        #    - The list of levels using result[::-1]
        #    - Each level individually using level[::-1]
        # 3. Result: leaf-level first with rightmost nodes first at each level
        #
        # Use case: Tree processing from leaves to root with right-to-left directionality
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level (left to right initially)
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

    def reverse_even_levels(self):
        # Reverses nodes at even-indexed levels (0, 2, 4, ...) while keeping odd levels unchanged
        # Performs standard BFS collection then selectively reverses even-indexed levels
        #
        # Algorithm:
        # 1. Perform standard BFS traversal from root to leaves, collecting each level
        # 2. For each level at index i in result:
        #    a. If i is even (0, 2, 4, ...), reverse that level using [::-1]
        #    b. If i is odd (1, 3, 5, ...), keep the level unchanged
        # 3. Return result with alternating normal and reversed levels
        #
        # Use case: Zigzag-like traversal where even levels display right-to-left
        # This creates a pattern: Level 0 (reversed), Level 1 (normal), Level 2 (reversed), ...
        #
        # Example tree:
        #         1
        #        / \
        #       2   3
        #      / \ / \
        #     4  5 6  7
        # Returns: [[1], [2, 3], [7, 6, 5, 4]]
        # Level 0 (even): [1] reversed to [1] (single element)
        # Level 1 (odd):  [2, 3] unchanged
        # Level 2 (even): [4, 5, 6, 7] reversed to [7, 6, 5, 4]
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.value)

                # Add children to queue for next level (left first maintains standard order)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        # Reverse only even-indexed levels (0, 2, 4, ...)
        # Use enumerate to track level index
        return [level[::-1] if i % 2 == 0 else level for i, level in enumerate(result)]

    def POST_RUN_SUMMARY(self):
        # POST_RUN_SUMMARY for BinaryTree class
        # Comprehensive summary of all tree traversal and reversal methods implemented
        #
        # This class provides 9 distinct traversal methods supporting both forward and reverse directions:
        #
        # Level-Order Traversals (BFS-based):
        # - level_order_traversal_left_to_right: Top-to-bottom, left-to-right per level
        #   Uses deque with standard left-child-first enqueuing order
        #   Returns: [[1], [2, 3], [4, 5, 6, 7]]
        #
        # - level_order_traversal_right_to_left: Top-to-bottom, right-to-left per level
        #   Collects nodes left-to-right but reverses each level for display
        #   Returns: [[1], [3, 2], [7, 6, 5, 4]]
        #
        # - reverse_level_order_traversal: Bottom-to-top, left-to-right per level
        #   Reverses the entire level list after BFS collection
        #   Returns: [[4, 5, 6, 7], [2, 3], [1]]
        #
        # - reverse_level_order_traversal_right_to_left: Bottom-to-top, right-to-left per level
        #   Combines full list reversal with individual level reversal
        #   Returns: [[7, 6, 5, 4], [3, 2], [1]]
        #
        # - reverse_even_levels: Top-to-bottom with alternating level reversal
        #   Reverses only even-indexed levels (0, 2, 4, ...) while keeping odd levels normal
        #   Returns: [[1], [2, 3], [7, 6, 5, 4]]
        #
        # Depth-First Traversals (Recursive DFS):
        # - reverse_inorder_traversal: Right -> Node -> Left (reverse of left->node->right)
        #   Returns: [7, 6, 5, 4, 3, 2, 1]
        #
        # - reverse_preorder_traversal: Node -> Right -> Left (processes node first)
        #   Returns: [1, 3, 7, 6, 2, 5, 4]
        #
        # - reverse_postorder_traversal: Right -> Left -> Node (processes node last)
        #   Returns: [7, 6, 3, 5, 4, 2, 1]
        #
        # Performance Characteristics:
        # - Time Complexity: O(n) for all methods - each node visited exactly once
        # - Space Complexity: O(w) for BFS (w=max level width), O(h) for DFS (h=tree height)
        #
        # Implementation Details:
        # - BFS methods use deque from collections for O(1) append/popleft operations
        # - DFS methods use recursive helpers to maintain clean traversal logic
        # - List reversals ([::-1]) perform in O(n) time with Python's optimized implementation
        # - No external dependencies beyond Python's built-in collections module
        #
        # Example Tree Structure Used in Testing:
        #         1
        #        / \
        #       2   3
        #      / \ / \
        #     4  5 6  7
        #
        return {
            "class": "BinaryTree",
            "purpose": "Complete binary tree traversal with forward and reverse options",
            "methods_count": 9,
            "traversal_types": ["level-order", "depth-first"],
            "directions": ["left-to-right", "right-to-left", "top-to-bottom", "bottom-to-top", "alternating"],
            "time_complexity": "O(n)",
            "space_complexity": "O(w) or O(h)",
            "key_feature": "Comprehensive reversal capabilities including level-selective reversal"
        }

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
