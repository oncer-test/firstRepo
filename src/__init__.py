"""
Reverse Backward Node Algorithm Package

This package provides a complete implementation of the reverse backward node algorithm,
including Node class for tree/graph structures and traversal algorithms.

Exports:
    Node: Tree node class
    ReverseBackwardTraversal: Traversal algorithm implementation
    build_example_tree: Helper function to create example trees
"""

from .reverse_backward_node import (
    Node,
    ReverseBackwardTraversal,
    build_example_tree,
)

__all__ = [
    'Node',
    'ReverseBackwardTraversal',
    'build_example_tree',
]

__version__ = '1.0'
__author__ = 'Algorithm Implementation Module'
__license__ = 'MIT'
