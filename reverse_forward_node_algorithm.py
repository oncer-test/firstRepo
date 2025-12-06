"""
Reverse Forward Node Algorithm Implementation

This module implements the Reverse Forward Node algorithm, commonly used in:
- Automatic Differentiation (AD): Computing gradients of scalar functions
- Computational Graphs: Forward pass computes values, reverse pass computes derivatives
- Dynamic Programming: Propagating values and dependencies through a DAG
- Neural Networks: Backpropagation for training deep learning models

Algorithm Overview:
    1. FORWARD PASS: Traverse nodes in topological order, compute intermediate values
    2. REVERSE PASS: Traverse nodes in reverse topological order, compute gradients/dependencies

Time Complexity: O(V + E) for both forward and reverse passes, where V = vertices, E = edges
Space Complexity: O(V) to store node values and gradients

Example:
    Simple computation: z = (x + y) * x
    Forward pass: x=2, y=3 → a=5 → z=10
    Reverse pass: ∂z/∂z=1 → ∂z/∂a=2, ∂z/∂x=5 → ∂z/∂y=2

Author: Claude Code
License: MIT
"""

from typing import List, Dict, Tuple, Optional, Any
from collections import defaultdict, deque


class Node:
    """
    Represents a node in a computational graph.

    Each node can store:
    - value: The computed value in the forward pass
    - gradient: The computed gradient in the reverse pass
    - children: Nodes that depend on this node (forward dependencies)
    - parents: Nodes this node depends on (input dependencies)

    Attributes:
        name (str): Unique identifier for the node
        value (float): Result of forward pass computation
        gradient (float): Result of reverse pass computation (derivative/contribution)
        parents (List[Node]): Input nodes this node depends on
        children (List[Node]): Output nodes that depend on this node
        operation (str): Description of the operation (e.g., 'add', 'multiply', 'input')

    Example:
        >>> node_x = Node("x", operation="input")
        >>> node_y = Node("y", operation="input")
        >>> node_z = Node("z", operation="add")
        >>> node_z.parents = [node_x, node_y]
        >>> node_x.children.append(node_z)
        >>> node_y.children.append(node_z)
    """

    def __init__(self, name: str, operation: str = "input") -> None:
        """
        Initialize a node in the computational graph.

        Args:
            name: Unique identifier for the node
            operation: Type of operation this node performs (default: "input" for leaf nodes)
        """
        self.name: str = name
        self.value: Optional[float] = None
        self.gradient: float = 0.0
        self.parents: List['Node'] = []
        self.children: List['Node'] = []
        self.operation: str = operation

    def __repr__(self) -> str:
        """Return string representation of the node."""
        return f"Node({self.name}, op={self.operation}, val={self.value}, grad={self.gradient})"

    def add_parent(self, parent: 'Node') -> None:
        """Add a parent (input) node and update child reference."""
        if parent not in self.parents:
            self.parents.append(parent)
        if self not in parent.children:
            parent.children.append(self)

    def clear_gradients(self) -> None:
        """Reset gradient to zero."""
        self.gradient = 0.0


class ComputationGraph:
    """
    Manages a computational graph and performs forward/reverse passes.

    This class handles the complete lifecycle of forward and reverse computation:
    - Building the graph structure
    - Executing forward pass (bottom-up traversal)
    - Executing reverse pass (top-down traversal)
    - Computing topological order for correct execution

    Attributes:
        nodes (Dict[str, Node]): Mapping from node names to Node objects
        output_node (Optional[Node]): The final output node for reverse pass

    Example:
        >>> graph = ComputationGraph()
        >>> x = graph.add_node("x")
        >>> y = graph.add_node("y")
        >>> z = graph.add_operation("z", "add", [x, y])
        >>> graph.forward_pass({"x": 2.0, "y": 3.0}, "z")
        >>> print(graph.nodes["z"].value)  # Output: 5.0
    """

    def __init__(self) -> None:
        """Initialize an empty computation graph."""
        self.nodes: Dict[str, Node] = {}
        self.output_node: Optional[Node] = None

    def add_node(self, name: str, operation: str = "input") -> Node:
        """
        Add a node to the computation graph.

        Args:
            name: Unique identifier for the node
            operation: Type of operation (default: "input")

        Returns:
            The newly created Node object

        Raises:
            ValueError: If node with this name already exists
        """
        if name in self.nodes:
            raise ValueError(f"Node '{name}' already exists in graph")
        node = Node(name, operation)
        self.nodes[name] = node
        return node

    def add_operation(self, output_name: str, op_type: str,
                     input_names: List[str]) -> Node:
        """
        Add an operation node that depends on input nodes.

        Args:
            output_name: Name of the output node
            op_type: Type of operation ('add', 'multiply', 'square', etc.)
            input_names: Names of input nodes for this operation

        Returns:
            The newly created operation Node

        Raises:
            ValueError: If input nodes don't exist or output node already exists
        """
        # Validate input nodes exist
        for name in input_names:
            if name not in self.nodes:
                raise ValueError(f"Input node '{name}' does not exist")

        # Create output node
        output_node = self.add_node(output_name, operation=op_type)

        # Connect parents
        for name in input_names:
            output_node.add_parent(self.nodes[name])

        return output_node

    def _topological_sort(self, start_node: Node) -> List[Node]:
        """
        Compute topological ordering of nodes from start_node to leaves.

        Uses depth-first search to order nodes such that parents appear before children.
        This ensures correct computation order during forward pass.

        Args:
            start_node: The root node to start traversal from

        Returns:
            List of nodes in topological order (parents before children)
        """
        visited = set()
        topo_order = []

        def dfs(node: Node) -> None:
            """Depth-first search helper for topological sort."""
            if node in visited:
                return
            visited.add(node)
            # Visit parents first (dependencies)
            for parent in node.parents:
                dfs(parent)
            # Add current node after its dependencies
            topo_order.append(node)

        dfs(start_node)
        return topo_order

    def _reverse_topological_sort(self, start_node: Node) -> List[Node]:
        """
        Compute reverse topological ordering of nodes from start_node to roots.

        Used for reverse pass traversal. Ensures children are processed before parents.

        Args:
            start_node: The output node to start traversal from

        Returns:
            List of nodes in reverse topological order (children before parents)
        """
        visited = set()
        reverse_topo_order = []

        def dfs(node: Node) -> None:
            """Depth-first search helper for reverse topological sort."""
            if node in visited:
                return
            visited.add(node)
            # Visit children first
            for child in node.children:
                dfs(child)
            # Add current node after its children
            reverse_topo_order.append(node)

        dfs(start_node)
        return reverse_topo_order

    def forward_pass(self, inputs: Dict[str, float], output_name: str) -> float:
        """
        Execute forward pass to compute all node values.

        Traverses the graph in topological order from input nodes to the output node,
        computing intermediate values using operation-specific logic.

        Args:
            inputs: Dictionary mapping input node names to their values
            output_name: Name of the output node to compute

        Returns:
            The computed value of the output node

        Raises:
            ValueError: If output node doesn't exist or inputs are missing
            NotImplementedError: If operation type is not supported
        """
        # Validate output node exists
        if output_name not in self.nodes:
            raise ValueError(f"Output node '{output_name}' does not exist")

        output_node = self.nodes[output_name]

        # Get topological order
        topo_order = self._topological_sort(output_node)

        # Set input values
        for name, value in inputs.items():
            if name not in self.nodes:
                raise ValueError(f"Input node '{name}' does not exist")
            self.nodes[name].value = value

        # Compute each node in order
        for node in topo_order:
            if node.operation == "input":
                # Input nodes already have their values set
                continue
            elif node.operation == "add":
                # Addition: sum all parent values
                node.value = sum(parent.value for parent in node.parents)
            elif node.operation == "multiply":
                # Multiplication: product of all parent values
                result = 1.0
                for parent in node.parents:
                    result *= parent.value
                node.value = result
            elif node.operation == "square":
                # Square: parent^2 (assumes single parent)
                if len(node.parents) != 1:
                    raise ValueError(f"Square operation requires exactly 1 parent, got {len(node.parents)}")
                node.value = node.parents[0].value ** 2
            elif node.operation == "negate":
                # Negation: -parent (assumes single parent)
                if len(node.parents) != 1:
                    raise ValueError(f"Negate operation requires exactly 1 parent, got {len(node.parents)}")
                node.value = -node.parents[0].value
            else:
                raise NotImplementedError(f"Operation '{node.operation}' not implemented")

        self.output_node = output_node
        return output_node.value

    def reverse_pass(self) -> Dict[str, float]:
        """
        Execute reverse pass to compute all node gradients.

        Starting from the output node with gradient = 1.0, propagates gradients
        backwards through the graph using the chain rule. Each parent accumulates
        contributions from all its children.

        Returns:
            Dictionary mapping node names to their computed gradients

        Raises:
            RuntimeError: If forward_pass hasn't been called yet
            NotImplementedError: If operation type is not supported
        """
        if self.output_node is None:
            raise RuntimeError("Must call forward_pass() before reverse_pass()")

        # Clear all gradients
        for node in self.nodes.values():
            node.clear_gradients()

        # Set output gradient to 1.0 (d(output)/d(output) = 1)
        self.output_node.gradient = 1.0

        # Collect all reachable nodes and topologically sort them
        all_nodes = set()

        def collect_nodes(node: Node) -> None:
            """Collect all nodes reachable from the output."""
            if node in all_nodes:
                return
            all_nodes.add(node)
            for parent in node.parents:
                collect_nodes(parent)

        collect_nodes(self.output_node)

        # Create reverse topological order: parents before children (for gradient propagation)
        visited = set()
        rev_topo = []

        def dfs_reverse(node: Node) -> None:
            """Build reverse topological order using DFS."""
            if node in visited:
                return
            visited.add(node)
            # Visit parents first, then add node
            for parent in node.parents:
                dfs_reverse(parent)
            rev_topo.append(node)

        dfs_reverse(self.output_node)

        # Reverse the order so we process from output to inputs
        rev_topo.reverse()

        # Backpropagate gradients
        for node in rev_topo:
            if node.operation == "input":
                # Leaf nodes: no further backprop
                continue
            elif node.operation == "add":
                # Addition: d(output)/d(parent) = d(output)/d(node) for each parent
                # (derivative of sum w.r.t each input is 1)
                for parent in node.parents:
                    parent.gradient += node.gradient
            elif node.operation == "multiply":
                # Multiplication: product rule
                # For z = x * y: dz/dx = y, dz/dy = x
                # For multiple: dz/dx_i = product of all other parents
                for i, parent in enumerate(node.parents):
                    # Compute product of all parents except this one
                    other_product = 1.0
                    for j, other_parent in enumerate(node.parents):
                        if i != j:
                            other_product *= other_parent.value
                    parent.gradient += node.gradient * other_product
            elif node.operation == "square":
                # Square: d(x^2)/dx = 2x
                parent = node.parents[0]
                parent.gradient += node.gradient * 2.0 * parent.value
            elif node.operation == "negate":
                # Negation: d(-x)/dx = -1
                parent = node.parents[0]
                parent.gradient += node.gradient * (-1.0)
            else:
                raise NotImplementedError(f"Operation '{node.operation}' not implemented")

        # Return gradients as dictionary
        return {name: node.gradient for name, node in self.nodes.items()}


def example_simple_addition() -> None:
    """
    Example 1: Simple Addition

    Compute: z = x + y
    Forward: x=2, y=3 → z=5
    Reverse: ∂z/∂x=1, ∂z/∂y=1
    """
    print("\n=== Example 1: Simple Addition ===")
    print("Computation: z = x + y")

    graph = ComputationGraph()
    graph.add_node("x")
    graph.add_node("y")
    graph.add_operation("z", "add", ["x", "y"])

    # Forward pass
    result = graph.forward_pass({"x": 2.0, "y": 3.0}, "z")
    print(f"Forward Pass: x=2, y=3 → z={result}")

    # Reverse pass
    gradients = graph.reverse_pass()
    print(f"Reverse Pass: ∂z/∂x={gradients['x']}, ∂z/∂y={gradients['y']}")
    print(f"Note: Both gradients are 1.0 because dz/dx = 1 and dz/dy = 1")


def example_multiplication_chain() -> None:
    """
    Example 2: Multiplication and Chain Rule

    Compute: z = (x + y) * x
    Forward: x=2, y=3 → a=5 → z=10
    Reverse: ∂z/∂a=2, ∂z/∂x=a+x=7, ∂z/∂y=2 (chain rule applies)
    """
    print("\n=== Example 2: Multiplication and Chain Rule ===")
    print("Computation: z = (x + y) * x")

    graph = ComputationGraph()
    graph.add_node("x")
    graph.add_node("y")
    graph.add_operation("a", "add", ["x", "y"])
    graph.add_operation("z", "multiply", ["a", "x"])

    # Forward pass
    result = graph.forward_pass({"x": 2.0, "y": 3.0}, "z")
    print(f"Forward Pass: x=2, y=3 → a=5 → z={result}")

    # Reverse pass
    gradients = graph.reverse_pass()
    print(f"Reverse Pass: ∂z/∂x={gradients['x']}, ∂z/∂y={gradients['y']}")
    print(f"Note: ∂z/∂x = ∂z/∂a * ∂a/∂x + ∂z/∂z * ∂z/∂x = 2*1 + 1*5 = 7")
    print(f"      ∂z/∂y = ∂z/∂a * ∂a/∂y = 2*1 = 2")


def example_quadratic() -> None:
    """
    Example 3: Quadratic Function

    Compute: z = x^2 + 2*x*y + y^2 = (x + y)^2
    Forward: x=2, y=1 → a=4, b=4, c=1 → z=9
    Reverse: ∂z/∂x=6, ∂z/∂y=6 (derivative of (x+y)^2 = 2(x+y))
    """
    print("\n=== Example 3: Quadratic Function ===")
    print("Computation: z = x^2 + 2*x*y + y^2 (which equals (x+y)^2)")

    graph = ComputationGraph()
    graph.add_node("x")
    graph.add_node("y")

    # x^2
    graph.add_operation("x_sq", "square", ["x"])

    # y^2
    graph.add_operation("y_sq", "square", ["y"])

    # 2*x*y
    graph.add_node("two")
    graph.add_operation("x_times_y", "multiply", ["x", "y"])
    graph.add_operation("two_xy", "multiply", ["two", "x_times_y"])

    # Sum all terms
    graph.add_operation("z", "add", ["x_sq", "y_sq", "two_xy"])

    # Forward pass
    result = graph.forward_pass({"x": 2.0, "y": 1.0, "two": 2.0}, "z")
    print(f"Forward Pass: x=2, y=1 → z={result}")

    # Reverse pass
    gradients = graph.reverse_pass()
    print(f"Reverse Pass: ∂z/∂x={gradients['x']}, ∂z/∂y={gradients['y']}")
    print(f"Note: z = (x+y)^2, so ∂z/∂x = 2(x+y) = {2*(2+1)}, ∂z/∂y = 2(x+y) = {2*(2+1)}")


def example_neural_network_like() -> None:
    """
    Example 4: Neural Network-like Computation

    Compute: z = (w1*x1 + b1)^2 + (w2*x2 + b2)^2
    (Simple model with two neurons and squared loss)
    """
    print("\n=== Example 4: Neural Network-like Computation ===")
    print("Computation: z = (w1*x1 + b1)^2 + (w2*x2 + b2)^2")

    graph = ComputationGraph()

    # Inputs and parameters
    graph.add_node("x1")
    graph.add_node("x2")
    graph.add_node("w1")
    graph.add_node("w2")
    graph.add_node("b1")
    graph.add_node("b2")

    # First neuron: z1 = (w1*x1 + b1)^2
    graph.add_operation("w1x1", "multiply", ["w1", "x1"])
    graph.add_operation("z1_linear", "add", ["w1x1", "b1"])
    graph.add_operation("z1", "square", ["z1_linear"])

    # Second neuron: z2 = (w2*x2 + b2)^2
    graph.add_operation("w2x2", "multiply", ["w2", "x2"])
    graph.add_operation("z2_linear", "add", ["w2x2", "b2"])
    graph.add_operation("z2", "square", ["z2_linear"])

    # Total loss: z = z1 + z2
    graph.add_operation("z", "add", ["z1", "z2"])

    # Forward pass
    inputs = {"x1": 1.0, "x2": 2.0, "w1": 0.5, "w2": 0.3, "b1": 0.1, "b2": 0.2}
    result = graph.forward_pass(inputs, "z")
    print(f"Forward Pass with inputs {inputs}")
    print(f"Output loss: z={result:.4f}")

    # Reverse pass
    gradients = graph.reverse_pass()
    print(f"Reverse Pass (computed gradients):")
    print(f"  ∂z/∂x1 = {gradients['x1']:.4f}")
    print(f"  ∂z/∂x2 = {gradients['x2']:.4f}")
    print(f"  ∂z/∂w1 = {gradients['w1']:.4f}")
    print(f"  ∂z/∂w2 = {gradients['w2']:.4f}")
    print(f"  ∂z/∂b1 = {gradients['b1']:.4f}")
    print(f"  ∂z/∂b2 = {gradients['b2']:.4f}")
    print(f"Note: Gradients are used for parameter updates in gradient descent")


if __name__ == "__main__":
    """
    Main entry point: Run all examples demonstrating the reverse forward algorithm.
    """
    print("=" * 70)
    print("REVERSE FORWARD NODE ALGORITHM - EXAMPLES")
    print("=" * 70)
    print("\nThis script demonstrates automatic differentiation using the")
    print("reverse forward node algorithm (also known as backpropagation).")
    print("\nThe algorithm has two phases:")
    print("  1. FORWARD PASS: Compute node values bottom-up from inputs to outputs")
    print("  2. REVERSE PASS: Compute gradients top-down from output to inputs")

    example_simple_addition()
    example_multiplication_chain()
    example_quadratic()
    example_neural_network_like()

    print("\n" + "=" * 70)
    print("END OF EXAMPLES")
    print("=" * 70)
