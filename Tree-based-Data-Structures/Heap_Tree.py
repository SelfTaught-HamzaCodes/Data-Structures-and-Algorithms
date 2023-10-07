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


class Heaps:

    def __init__(self, root=None, type_="max"):
        assert type_ in ["min", "max"], "Invalid type_, use 'min' for MIN-Heap and 'max' for MAX-Heap"

        self.type_ = type_
        self.root = root
        self.nodes = 0

    def insert(self, value):
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
                self.__heapify_insert(self.root, value=value, type_=self.type_)
                return

            # To add the right node of node=queue.popleft().
            if node.right:
                queue.append(node.right)

            # If node.right is not available, that means we have free space, and we place the value their.
            else:
                node.right = new_node
                self.__heapify_insert(self.root, value=value, type_=self.type_)
                return

    def __heapify_insert(self, node, value=None, type_='max'):

        # Limitations: might not work for duplicate values.

        if not node:
            return False

        if node.value == value:
            return True

        match = self.__heapify_insert(node.left, value=value, type_=type_)

        if match or node.left:
            if node.left.value == value:
                if type_ == 'max':
                    if value > node.value:
                        node.left.value, node.value = node.value, value
                        return

                else:
                    if value < node.value:
                        node.left.value, node.value = node.value, value
                        return

        match = self.__heapify_insert(node.right, value=value, type_=type_)

        if match or node.right:
            if node.right.value == value:
                if type_ == 'max':
                    if value > node.value:
                        node.right.value, node.value = node.value, value
                        return

                else:
                    if value < node.value:
                        node.right.value, node.value = node.value, value
                        return

        return False

    def delete(self):

        if not self.root.left and not self.root.right:
            self.root = None
            return

        queue = deque()
        queue.append(self.root)
        last_element = None

        # while len(queue) > 0.
        while queue:

            # queue.popleft() remove the left-most value and returns it.
            node = queue.popleft()

            # To add the left node of node=queue.popleft().
            if node.left:
                queue.append(node.left)

            # To add the right node of node=queue.popleft().
            if node.right:
                queue.append(node.right)

            # If node is None, then last item in the queue is queue[-1].
            else:
                last_element = queue[-1]
                break

        queue.clear()
        queue.append(self.root)

        while last_element:

            # queue.popleft() remove the left-most value and returns it.
            node = queue.popleft()

            # To add the left node of node=queue.popleft().
            if node.left:
                if node.left.value == last_element.value:
                    self.root.value, node.left = last_element.value, None
                    self.heapify_delete()
                    return

                queue.append(node.left)

            # To add the right node of node=queue.popleft().
            if node.right:
                if node.right.value == last_element.value:
                    self.root.value, node.right = last_element.value, None
                    self.heapify_delete()
                    return

                queue.append(node.right)

    def heapify_delete(self):

        value_to_be_traversed = self.root

        while True:
            left, right = value_to_be_traversed.left, value_to_be_traversed.right

            if left or right:

                if self.type_ == "max":
                    # if 2 nodes, root and left.
                    if value_to_be_traversed.value > left.value:
                        break

                    # self.root is the largest element:
                    elif self.root.value > left.value and self.root.value > right.value:
                        break

                    elif value_to_be_traversed.value < left.value and not right:
                        value_to_be_traversed.value, left.value = left.value, value_to_be_traversed.value
                        break

                    if left.value > right.value:
                        value_to_be_traversed.value, left.value = left.value, value_to_be_traversed.value
                        value_to_be_traversed = value_to_be_traversed.left

                    elif right.value > left.value:
                        value_to_be_traversed.value, right.value = right.value, value_to_be_traversed.value
                        value_to_be_traversed = value_to_be_traversed.right

                if self.type_ == "min":

                    # if 2 nodes, root and left.
                    if value_to_be_traversed.value < left.value:
                        break

                    # self.root is the largest element:
                    elif value_to_be_traversed.value < left.value and value_to_be_traversed.value < right.value:
                        break

                    elif value_to_be_traversed.value > left.value and not right:
                        value_to_be_traversed.value, left.value = left.value, value_to_be_traversed.value
                        break

                    if left.value < right.value:
                        value_to_be_traversed.value, left.value = left.value, value_to_be_traversed.value
                        value_to_be_traversed = value_to_be_traversed.left

                    elif right.value < left.value:
                        value_to_be_traversed.value, right.value = right.value, value_to_be_traversed.value
                        value_to_be_traversed = value_to_be_traversed.right
            break

    def search(self, value):

        if not self.root:
            return False

        elif self.root.value < value and self.type_ == "max":
            return False

        elif self.root.value > value and self.type_ == "min":
            return False

        queue = deque()
        queue.append(self.root)

        # while len(queue) > 0.
        while queue:

            # queue.popleft() remove the left-most value and returns it.
            node = queue.popleft()

            # To add the left node of node=queue.popleft().
            if node.left or node.right:

                if node.left.value == value:
                    return True

                if node.right and node.right.value == value:
                    return True

                if self.type_ == "max":
                    if node.left.value < value:
                        return False
                    elif node.right.value < value:
                        return False
                    else:
                        queue.append(node.left)
                        queue.append(node.right)

                if self.type_ == "min":
                    if node.left.value > value:
                        return False
                    elif node.right.value > value:
                        return False
                    else:
                        queue.append(node.left)
                        queue.append(node.right)

    def heap_sort(self):

        # Limitations deletes the tree.

        sorted_array = [self.root.value]

        while self.root:
            self.delete()
            if self.root:
                sorted_array.append(self.root.value)

        return sorted_array

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


if __name__ == "__main__":
    # Initialise a heap object.
    heap = Heaps(type_='max')

    # Insert values into our heap.
    heap.insert(5)
    heap.insert(3)
    heap.insert(4)
    heap.insert(2)
    heap.insert(6)

    # delete:
    heap.delete()

    # search:
    print(heap.search(2))

    # Using print() to print out different traversals for the same heap.
    print("In-Order:   ", heap.print_inorder())

    # sort:
    print(heap.heap_sort())
