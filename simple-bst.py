class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_root_val(self):
        if self.is_empty():
            return None
        else:
            return self.root.value

    def add_node_acc(self, val, node, parent_val=None):
        if node is None:
            return {"node": Node(val), "parent": parent_val} # parent_val is None at first, then holds parent's value as we continue recursively

        # recursively add value to left or right subtree depending on current node value, then update the current node's child
        if val < node.value:
            result = self.add_node_acc(val, node.left, node.value)
            node.left = result["node"]
        else:
            result = self.add_node_acc(val, node.right, node.value)
            node.right = result["node"]

        return {"node": node, "parent": result["parent"]}

    def add_node(self, val):
        if self.is_empty():
            self.root = Node(val)
            return None
        else:
            result = self.add_node_acc(val, self.root)
            self.root = result["node"]
            return result["parent"]

    def contains_acc(self, node, val):
        if node is None:
            return False
        if node.value == val:
            return True
        if val < node.value:
            return self.contains_acc(node.left, val)
        else:
            return self.contains_acc(node.right, val)

    def contains(self, val):
        return self.contains_acc(self.root, val)


# TESTING (Generated via LLM)
def run_tests():
    # Create a new tree
    tree = Tree()

    # Test empty tree
    print("Is empty: {} (Expected: True)".format(tree.is_empty()))
    print("Root value: {} (Expected: None)".format(tree.get_root_val()))

    # Add root node
    print("\nAdding root node:")
    print("Return value: {} (Expected: None)".format(tree.add_node(10)))
    print("Is empty: {} (Expected: False)".format(tree.is_empty()))
    print("Root value: {} (Expected: 10)".format(tree.get_root_val()))

    # Add multiple nodes
    print("\nAdding multiple nodes:")
    nodes_to_add = [5, 15, 3, 7, 12, 18]
    expected_returns = [10, 10, 5, 5, 15, 15]
    for node, expected in zip(nodes_to_add, expected_returns):
        return_val = tree.add_node(node)
        print(f"Added {node}, returned: {return_val} (Expected: {expected})")

    # Final root value
    print("\nFinal root value: {} (Expected: 10)".format(tree.get_root_val()))

    # Check if values are present
    print("\nChecking for presence of values:")
    values_to_check = [3, 7, 10, 12, 18, 4, 13, 20]
    expected_results = [True, True, True, True, True, False, False, False]
    for value, expected in zip(values_to_check, expected_results):
        result = tree.contains(value)
        print(f"Contains {value}: {result} (Expected: {expected})")

    # Demonstrate adding a duplicate value
    print("\nAdding a duplicate value:")
    duplicate_val = 7
    return_val = tree.add_node(duplicate_val)
    print(f"Added {duplicate_val}, returned: {return_val} (Expected: 5)")

    # Check the structure by adding nodes in a specific order
    print("\nChecking tree structure:")
    new_tree = Tree()
    structure_nodes = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    expected_returns = [None, 8, 8, 3, 3, 10, 6, 6, 14]
    for node, expected in zip(structure_nodes, expected_returns):
        return_val = new_tree.add_node(node)
        print(f"Added {node}, returned: {return_val} (Expected: {expected})")


if __name__ == "__main__":
    run_tests()
