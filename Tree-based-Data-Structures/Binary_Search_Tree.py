"""
An Implementation of a Binary Search Tree.
"""

from Binary_Tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    A Binary Search Tree is an extension of the Binary Tree.

    This datastructure functions almost as identical to a Binary Tree but with one key difference.
        Once the root has been set.

        Any value greater than root, goes to the root.right.
        Any value smaller than root, goes to the root.left.

        Any values that follow, will go through the same principal, an imaginary root could be considered.

    Time Complexity:
    Best / Average: 0(log(n))
    Worst: 0(n)

    The worst case:
        this can be encountered, if we add values successive values greater than before,
        essentially makes a linked list.
        (root) 5 --> (right) 6 --> (right) 7 --> (right) 8.
    """

    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, value):
        """
        Insert values into our binary search tree.

        :param value: a value to be inserted, will automatically call Node and pass value.
        :return: None
        """

        # If root is None, we set the node it to Node(value)
        if not self.root:
            self.root = Node(value)
            self.nodes += 1
            return

        self.__insert_helper(self.root, value)

    def __insert_helper(self, node, value):
        """
        A helper function to insert values into our binary search tree.
        """

        # Base Case-A, if any empty node is found:
        if not node:
            self.nodes += 1
            return Node(value)

        # Base Case-B:
        if node.value == value:
            raise KeyError(value, "already exists.")

        # If value to be inserted is greater than current node's value, we traverse right, else left.
        if value > node.value:
            node.right = self.__insert_helper(node.right, value)
        else:
            node.left = self.__insert_helper(node.left, value)

        return node

    def search(self, value):
        """
        To search for a value within our binary tree.

        :param value: a value to be searched.
        :returns: True if value is found, else returns False.
        """
        return self.__search_helper(self.root, value)

    def __search_helper(self, node, value_to_search):
        """
        A helper function to search for a value.
        """

        # if node is None, then it means we traversed through all possible values and not found our value.
        if node:

            # Base Case-A: if value is located.
            if node.value == value_to_search:
                return True

            # else depending on the value traverse ahead accordingly.
            if value_to_search > node.value:
                return self.__search_helper(node.right, value_to_search)
            else:
                return self.__search_helper(node.left, value_to_search)

        return False


if __name__ == "__main__":
    # Initialise a binary search tree object.
    bst = BinarySearchTree()

    # Insert values into our binary search tree.
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(1)
    bst.insert(2)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    bst.insert(9)
    bst.insert(10)

    # Searching for a value:
    print(bst.search(10))  # Exists.
    print(bst.search(11))  # Not Exists.

    # Deleting a value from our binary search tree.
    bst.delete(1)

    # Using print() to print out different traversals for the same binary search tree.
    print("Pre-Order:  ", bst.print_preorder())
    print("In-Order:   ", bst.print_inorder())
    print("Post-Order: ", bst.print_postorder())
    print("Level-Order:", bst.print_level_order())

    # Using len() to print out the total number of nodes in my binary search tree.
    print(len(bst))
