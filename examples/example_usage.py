"""
Example Usage and Demonstrations of the Reverse Backward Node Algorithm

This module demonstrates various ways to use the Node and ReverseBackwardTraversal
classes for different real-world scenarios.

Examples include:
    1. Basic tree construction and traversal
    2. File system directory traversal simulation
    3. Expression tree evaluation (post-order)
    4. Computing subtree properties
    5. Memory cleanup patterns
"""

import sys

# Add src directory to path
sys.path.insert(0, '/Users/altyni/oncer/.local-workspaces/1a8c00d2-2cac-4232-8d16-7f452de83d30')

from src.reverse_backward_node import Node, ReverseBackwardTraversal


def example_1_basic_tree():
    """
    Example 1: Basic Tree Construction and Traversal

    Demonstrates creating a simple tree and traversing it using
    different methods provided by the algorithm.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Tree Construction and Traversal")
    print("=" * 70)

    # Create a simple tree
    root = Node("Root")
    left_subtree = Node("Left Subtree")
    right_subtree = Node("Right Subtree")
    left_child1 = Node("Left Child 1")
    left_child2 = Node("Left Child 2")

    # Build tree structure
    root.add_child(left_subtree)
    root.add_child(right_subtree)
    left_subtree.add_child(left_child1)
    left_subtree.add_child(left_child2)

    # Perform traversal
    traversal = ReverseBackwardTraversal()
    result = traversal.traverse_recursive(root)

    print("\nTree Structure:")
    print("       Root")
    print("       /  \\")
    print("      /    \\")
    print("    Left   Right")
    print("    /  \\")
    print("   C1  C2")

    print(f"\nPost-order Traversal Result: {result}")
    print("Order: Children before parents - left subtree, then right subtree, then root")


def example_2_file_system():
    """
    Example 2: File System Directory Tree Traversal

    Simulates a file system directory structure and performs
    post-order traversal (useful for cleanup operations like
    deleting directories - must delete files/subdirs before parent).
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: File System Directory Traversal")
    print("=" * 70)

    # Create a simulated file system
    root = Node("/home/user")
    documents = Node("Documents")
    pictures = Node("Pictures")
    work = Node("Work")

    root.add_child(documents)
    root.add_child(pictures)
    documents.add_child(work)

    traversal = ReverseBackwardTraversal()
    traversal_order = traversal.traverse_recursive(root)

    print("\nFile System Structure:")
    print("/home/user/")
    print("├── Documents/")
    print("│   └── Work/")
    print("└── Pictures/")

    print(f"\nDeletion Order (post-order): {traversal_order}")
    print("Why post-order? Delete deepest files/directories first,")
    print("then work up to parent directories. Parent can't be deleted")
    print("until all children are removed.")


def example_3_expression_tree():
    """
    Example 3: Expression Tree Evaluation

    Uses post-order traversal to evaluate a mathematical expression tree.
    Example: (3 + 4) * (5 - 2) -> Node structure with operators and operands.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Expression Tree Evaluation")
    print("=" * 70)

    # Create expression tree for: (3 + 4) * (5 - 2)
    multiply = Node("*")
    add = Node("+")
    subtract = Node("-")
    three = Node("3")
    four = Node("4")
    five = Node("5")
    two = Node("2")

    multiply.add_child(add)
    multiply.add_child(subtract)
    add.add_child(three)
    add.add_child(four)
    subtract.add_child(five)
    subtract.add_child(two)

    traversal = ReverseBackwardTraversal()
    eval_order = traversal.traverse_recursive(multiply)

    print("\nExpression Tree for: (3 + 4) * (5 - 2)")
    print("         *")
    print("        / \\")
    print("       +   -")
    print("      / \\ / \\")
    print("     3  4 5  2")

    print(f"\nPost-order Evaluation Order: {eval_order}")
    print("Evaluation steps:")
    print("  1. Evaluate left subtree:  3 + 4 = 7")
    print("  2. Evaluate right subtree: 5 - 2 = 3")
    print("  3. Evaluate root:          7 * 3 = 21")
    print("\nNote: Post-order ensures operands are evaluated before operators.")


def example_4_subtree_height():
    """
    Example 4: Computing Subtree Heights

    Uses post-order traversal with a callback to compute the height
    of each subtree. This is a classic dynamic programming on trees problem.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Computing Subtree Heights")
    print("=" * 70)

    # Create a tree
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    root.add_child(node2)
    root.add_child(node3)
    node2.add_child(node4)
    node2.add_child(node5)

    # Compute heights using post-order traversal
    traversal = ReverseBackwardTraversal()

    # Store height for each node
    heights = {}

    def compute_height(node_value):
        """Callback to compute height during traversal."""
        # For leaf nodes, height is 0
        # For non-leaf, find the maximum height among children
        # Note: This is simplified for demonstration
        heights[node_value] = 0

    # Better approach: use recursive traversal with manual computation
    def compute_heights_recursive(node):
        if node is None:
            return -1

        max_child_height = -1
        for child in node.children:
            child_height = compute_heights_recursive(child)
            max_child_height = max(max_child_height, child_height)

        node_height = max_child_height + 1
        heights[node.value] = node_height
        return node_height

    compute_heights_recursive(root)

    print("\nTree Structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\")
    print("   4   5")

    print(f"\nNode Heights: {heights}")
    print("Height definition: longest path from node to any leaf")
    print("  Node 4: height = 0 (leaf)")
    print("  Node 5: height = 0 (leaf)")
    print("  Node 3: height = 0 (leaf)")
    print("  Node 2: height = 1 (one level to leaves 4,5)")
    print("  Node 1: height = 2 (two levels to leaves 4,5)")


def example_5_memory_cleanup():
    """
    Example 5: Memory Cleanup Pattern

    Demonstrates how post-order traversal is useful for cleanup operations,
    such as freeing allocated resources or deallocating memory.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Memory Cleanup Pattern")
    print("=" * 70)

    # Simulate a tree of objects that need cleanup
    root = Node("Resource Manager")
    db_connection = Node("Database Connection")
    file_handle = Node("File Handle")
    memory_buffer = Node("Memory Buffer")

    root.add_child(db_connection)
    root.add_child(file_handle)
    root.add_child(memory_buffer)

    traversal = ReverseBackwardTraversal()
    cleanup_order = []

    # Use callback for cleanup simulation
    def cleanup_resource(resource_name):
        """Simulate resource cleanup."""
        cleanup_order.append(f"Cleanup: {resource_name}")

    traversal.traverse_with_callback(root, cleanup_resource)

    print("\nResource Hierarchy:")
    print("Resource Manager")
    print("├── Database Connection")
    print("├── File Handle")
    print("└── Memory Buffer")

    print("\nCleanup Order (post-order):")
    for action in cleanup_order:
        print(f"  {action}")

    print("\nWhy post-order for cleanup?")
    print("  • Parent manager depends on child resources")
    print("  • Clean up child resources first (they're still needed)")
    print("  • Clean up parent manager last (it manages cleanup)")


def example_6_iterative_vs_recursive():
    """
    Example 6: Comparing Iterative and Recursive Approaches

    Shows that both methods produce identical results and when to use each.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Iterative vs Recursive Traversal")
    print("=" * 70)

    # Create a tree
    root = Node(1)
    for i in range(2, 6):
        root.add_child(Node(i))

    traversal = ReverseBackwardTraversal()

    # Both methods
    recursive_result = traversal.traverse_recursive(root)
    iterative_result = traversal.traverse_iterative(root)

    print(f"\nRecursive Result:  {recursive_result}")
    print(f"Iterative Result:  {iterative_result}")
    print(f"Results Equal:     {recursive_result == iterative_result}")

    print("\nWhen to use each method:")
    print("  Recursive:")
    print("    ✓ Simpler, cleaner code")
    print("    ✓ Easier to understand and maintain")
    print("    ✗ Risk of stack overflow for very deep trees")
    print("\n  Iterative:")
    print("    ✓ No risk of stack overflow")
    print("    ✓ Better for very deep trees (100+ levels)")
    print("    ✗ Slightly more complex code")


def example_7_depth_grouping():
    """
    Example 7: Grouping Nodes by Depth Level

    Demonstrates traverse_by_depth for level-by-level analysis.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Grouping Nodes by Depth Level")
    print("=" * 70)

    # Create a tree with multiple levels
    root = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)

    traversal = ReverseBackwardTraversal()
    by_depth = traversal.traverse_by_depth(root)

    print("\nTree Structure:")
    print("       A")
    print("      / \\")
    print("     B   C")
    print("    / \\ /")
    print("   D  E F")

    print(f"\nNodes Grouped by Depth (bottom-up):")
    for level, nodes in enumerate(by_depth):
        print(f"  Level {level}: {nodes}")

    print("\nThis is useful for:")
    print("  • Level-order analysis")
    print("  • Layer-by-layer processing")
    print("  • Breadth-first style analysis from bottom-up")


def main():
    """Run all examples."""
    print("\n")
    print("#" * 70)
    print("# REVERSE BACKWARD NODE ALGORITHM - USAGE EXAMPLES")
    print("#" * 70)

    example_1_basic_tree()
    example_2_file_system()
    example_3_expression_tree()
    example_4_subtree_height()
    example_5_memory_cleanup()
    example_6_iterative_vs_recursive()
    example_7_depth_grouping()

    print("\n" + "=" * 70)
    print("EXAMPLES COMPLETED")
    print("=" * 70)
    print("\nFor more information, see:")
    print("  • src/reverse_backward_node.py - Full implementation and docstrings")
    print("  • tests/test_reverse_backward_node.py - Comprehensive test cases")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
