"""
An Implementation of a Binary Tree (Not Binary Search Tree):
"""

from collections import deque


class Node:
    """
    Initializes a Node, with a value, a left reference and a right reference.

    :param value: A value for our node.

    :param left: Reference to the left child (Node).

    :param right: Reference to the right child (Node).
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    A Binary Tree is an extension of the Linked List, where the Parent (Node) can have at max 2 children (nodes).

    :param root: On initialization set to None.
    :type root: Node

    :ivar root: This will hold the root of the binary tree.
    :type root: Node

    :ivar nodes: This will hold the total number of nodes in our binary tree.
    :type nodes: int
    """

    def __init__(self, root=None):
        self.root = root
        self.nodes = 0

    def __len__(self):
        """
        Returns the total number of nodes in our binary tree.

        :return __nodes:
        :type: int
        """
        return self.nodes

    def insert(self, value):
        """
        Insert values into our binary tree.

        This insert method uses the Level-Order Traversal Method to insert the Node(value) at the first available space.

        :param value: value to be entered into our binary tree.
        :return: None
        """

        # Convert our value to Node Object, and assign Node.value = value.
        new_node = Node(value)

        # Increment our total nodes by 1.
        self.nodes += 1

        # If self.root = None, binary tree is empty.
        if not self.root:
            self.root = new_node
            return

        queue = deque()
        queue.append(self.root)

        # while len(queue) > 0.
        while queue:

            # queue.popleft() remove the left-most value and returns it.
            node = queue.popleft()

            # To add the left node of node=queue.popleft().
            if node.left:
                queue.append(node.left)

            # If node.left is not available, that means we have free space, and we place the value their.
            else:
                node.left = new_node
                return

            # To add the right node of node=queue.popleft().
            if node.right:
                queue.append(node.right)

            # If node.right is not available, that means we have free space, and we place the value their.
            else:
                node.right = new_node
                return

    def delete(self, value):
        """
        Deletes a node with the given value from the binary tree.
        """
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(self, node, value):
        """
        Helper function to recursively delete a node with the given value.

        This helper function has 2 base cases:
            if not node, return None,
                if current node being processed is None.

            if node.value == value:
                Case 1: Node to be deleted is a leaf node.
                    return None, this will make the calling functions either left or right reference to None.
                Case 2: Node to be deleted has only one child.
                    return child node, this will make the calling function's either left or right reference to child.
                Case 3: Node to be deleted has two children.
                    - Choose a successor, the one that is on the right side.
                    - Loop the successor's left until, None is reached.
                    - Replace node's value (to be deleted) with the successor's value.
                    - Call function recursively, setting node as node's right and value to be the successor's value.
                    - This will trigger the base case 2, node to be deleted is a leaf node.

        Each call stack:
        node: being passed into the stack.
        node.left  = self._delete_helper(self, node.left, value), returns: _____
        node.right = self._delete_helper(self, node.right, value), returns: _____
        :rtype: node

        After a base-case is triggered, the respective node's reference gets changed.
        """

        # (Coming from) node(.left | .right) -> node is None, we reach base-case 1.
        # Returns None, to the node it came from.
        if not node:
            return node

        if node.value == value:

            # Case 1: Node to be deleted is a leaf node
            if not node.left and not node.right:

                # set the (coming from) node(.left |.right) to None.
                self.nodes -= 1
                return None

            # Case 2: Node to be deleted has only one child
            if not node.left or not node.right:

                # set the (coming from) node(.left | right) to the available child (the child != None).
                self.nodes -= 1
                return node.left if node.left else node.right

            # Case 3: Node to be deleted has two children, replace the node's value with the value of its inorder
            # successor, which is the leftmost node in its right subtree

            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value

            # Recursively delete the inorder successor from the right subtree
            node.right = self._delete_helper(node.right, successor.value)

        else:
            node.left = self._delete_helper(node.left, value)
            node.right = self._delete_helper(node.right, value)

        return node

    def print_preorder(self):
        """
        A function to traverse using pre-order traversal algorithm.

        Pre-order traversal is a type of tree traversal algorithm that starts at the root node and visits each node in
        the tree recursively, following a particular sequence. In pre-order traversal, the root node is visited first,
        followed by its left subtree, and then its right subtree.

        :return: traversed path.
        :rtype: str
        """
        return self.__preorder(self.root)

    def __preorder(self, root, traversal=""):
        """
        A helper function to recursively call and store the traversed path.

        :param root: current node being traversed.
        :type: Node

        :param traversal: a string to hold the traversed path.
        :type: str

        :return: the traversed path
        :rtype: str
        """

        # Base Case: If root is a node (not None).
        if root:
            traversal += (str(root.value) + "-")
            traversal = self.__preorder(root.left, traversal)
            traversal = self.__preorder(root.right, traversal)

        return traversal

    def print_inorder(self):
        """
        A function to traverse using in-order traversal algorithm.

        In-order traversal is a type of tree traversal algorithm that starts at the root node and visits each node in
        the tree recursively, following a particular sequence. In in-order traversal, the left subtree of the root is
        visited first, then the root node is visited, and finally the right subtree of the root is visited.

        :return: the traversed path
        :rtype: str
        """

        return self.__inorder(self.root)

    def __inorder(self, root, traversal=""):
        """
        A helper function to recursively call and store the traversed path.

        :param root: current node being traversed.
        :type: Node

        :param traversal: a string to hold the traversed path.
        :type: str

        :return: the traversed path
        :rtype: str
        """

        # Base Case: If root is a node (not None).
        if root:
            traversal = self.__inorder(root.left, traversal)
            traversal += str(root.value) + "-"
            traversal = self.__inorder(root.right, traversal)

        return traversal

    def print_postorder(self):
        """
        A function to traverse using post-order traversal algorithm.

        Postorder traversal is a type of tree traversal algorithm that starts at the root node and visits each node
        in the tree recursively, following a particular sequence. In postorder traversal, the left subtree of the
        root is visited first, then the right subtree of the root is visited, and finally the root node is visited.

        :return: the traversed path
        :rtype: str
        """
        return self.__postorder(self.root)

    def __postorder(self, root, traversal=""):
        """
        A helper function to recursively call and store the traversed path.

        :param root: current node being traversed.
        :type: Node

        :param traversal: a string to hold the traversed path.
        :type: str

        :return: the traversed path
        :rtype: str
        """

        # Base Case: If root is a node (not None).
        if root:
            traversal = self.__postorder(root.left, traversal)
            traversal = self.__postorder(root.right, traversal)
            traversal += str(root.value) + "-"

        return traversal

    def print_level_order(self):
        """
        A function to traverse using level-order traversal algorithm.

        Level-order traversal is a type of tree traversal algorithm that visits all the nodes of a tree level by
        level, starting from the root node. In level-order traversal, all the nodes at a given level are visited
        before moving on to the nodes at the next level. This traversal algorithm uses a queue data structure to keep
        track of the nodes to be visited.

        :return: the traversed path
        :rtype: str
        """

        queue = deque()
        queue.append(self.root)

        # To hold the traversed path.
        traversal = ""

        # while len(queue) > 0.
        while queue:
            node = queue.popleft()

            # As soon as a node is visited we add it to the traversal variable.
            traversal += str(node.value) + "-"

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return traversal


if __name__ == "__main__":

    # Initialise a binary tree object.
    bt = BinaryTree()

    # Insert values into our binary tree.
    bt.insert(0)
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)
    bt.insert(8)
    bt.insert(9)
    bt.insert(10)

    # Deleting a value from our binary tree.
    bt.delete(2)

    # Using print() to print out different traversals for the same binary tree.
    print("Pre-Order:  ", bt.print_preorder())
    print("In-Order:   ", bt.print_inorder())
    print("Post-Order: ", bt.print_postorder())
    print("Level-Order:", bt.print_level_order())

    # Using len() to print out the total number of nodes in my binary tree.
    print(len(bt))
