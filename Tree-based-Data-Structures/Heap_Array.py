class Heap:
    """
    A class representing a heap data structure.

    Attributes:
    -----------
    capacity : list
        A list representing the heap. Each element in the list is a value stored in the heap.
    order : str
        The order of the heap, either 'min' for a minimum heap or 'max' for a maximum heap.
    popped : int
        The number of elements removed from the heap since it was last re-ordered.

    Methods:
    --------
    _parent_index(child_index: int) -> int
        Given the index of a child node, return the index of its parent node.
    _child_left(parent_index: int) -> int
        Given the index of a parent node, return the index of its left child node.
    _child_right(parent_index: int) -> int
        Given the index of a parent node, return the index of its right child node.
    _check_siblings(index1: int, value1: Any, index2: int, value2: Any, order: str) -> int
        Given the indices and values of two sibling nodes and the order of the heap, return the index of the
        sibling node with the smaller or greater value depending on the order.
    capacity_check() -> bool
        Check if the heap is full and raise an OverflowError if so, otherwise return True.
    insert(value: Any) -> None
        Insert a value into the heap.
    delete() -> None
        Remove the root element of the heap.
    heap_sort() -> List
        Sort the heap in ascending or descending order and return the sorted list.
    """

    def __init__(self, capacity=5, order='min'):

        """
        Initializes a heap object with given capacity and order.

        Args:
            capacity (int): The maximum capacity of the heap. Default is 5.
            order (str): The order of the heap, can be 'min' for min-heap or 'max' for max-heap. Default is 'min'.

        Raises:
            AssertionError: If capacity is not a positive integer or order is not 'min' or 'max'.

        What is the use of self.popped ?
            Once our object in initialized, a list with the capacity specified is created (default: 5).
            This variable will hold the number of times, delete() function was called.
            Once our self.capacity is filled only then delete() can be called.
            The self.popped will increment by 1 everytime, delete() is called.
            We will switch the first element (root element) with array[-self.popped],
            this will give move elements (to the first element to the end of current not popped array).

        """

        assert (isinstance(capacity, int) and capacity > 0), "Capacity can only be a positive integer."
        assert order in ['min', 'max'], "Order can only be 'min' for min-heap and 'max' for max-heap"

        self.capacity = [None]*capacity
        self.order = order
        self.popped = 0

    def __str__(self):
        """
        Returns a string representation of the heap.

        Returns:
            str: A string representation of the heap, with a view of the non-popped elements.
        """
        return str(self.capacity[:-self.popped])

    @staticmethod
    def _parent_index(child_index):
        """
        Returns the index of the parent of a given child index.

        Args:
            child_index (int): The index of the child node.

        Returns:
            int: The index of the parent node.
        """
        return (child_index-1) // 2

    @staticmethod
    def _child_left(parent_index):
        """
        Returns the index of the left child of a given parent index.

        Args:
            parent_index (int): The index of the parent node.

        Returns:
            int: The index of the left child node.
        """
        return 2*parent_index + 1

    @staticmethod
    def _child_right(parent_index):
        """
        Returns the index of the right child of a given parent index.

        Args:
            parent_index (int): The index of the parent node.

        Returns:
            int: The index of the right child node.
        """
        return 2*parent_index + 2

    @staticmethod
    def _check_siblings(left_idx, left_val, right_idx, right_val, order):
        """
        Checks the siblings of the node at the given index
        and returns the index of the smaller or greater sibling based on the order.

        Args:
            left_idx (int): The index of the left sibling node.
            left_val (int): The value of the left sibling node.
            right_idx (int): The index of the right sibling node.
            right_val (int): The value of the right sibling node.
            order (str): The order of the heap, can be 'min' for min-heap or 'max' for max-heap.

        Returns:
            int: The index of the smaller or greater sibling node based on the order.
        """
        # If left_val is None or If right_val is None, we skip this part.
        # We can get None, if node has no right reference.
        if left_val and right_val:

            if order == 'min':
                return left_idx if left_val < right_val else right_idx
            if order == 'max':
                return left_idx if left_val > right_val else right_idx

        if left_val:
            return left_idx

        if right_val:
            return right_idx

    def capacity_check(self):
        """
        Checks if all the spaces in the heap array are filled.

        If any space in the heap array is not filled, raises an OverflowError
        with the message "Array is not completely filled." and the current heap
        capacity. Returns True if all spaces are filled.
        """
        for space in self.capacity:

            if not space:
                raise OverflowError(F"Array is not completely filled.", self.capacity)

        else:
            return True

    def insert(self, value):
        """
        Inserts a value into the heap and maintains the heap property.

        Args:
            value: A numeric value to be inserted into the heap.

        Raises:
            OverflowError: If the maximum capacity of the heap is reached.

        Returns:
            None
        """
        for index, space in enumerate(self.capacity):
            if not space:
                self.capacity[index] = value
                value_at_index = index
                break
        else:
            raise OverflowError(F"Max Capacity: {len(self.capacity)} is reached.")

        # From Right --> Left, the leftmost element will be at array[0], so after that we break-out.
        while value_at_index > 0:

            # Find Parent:
            parent_index = self._parent_index(child_index=value_at_index)

            # Out-of bounds, are index of the root cannot be less than 0.
            if parent_index < 0:
                break

            # If parent > 0, we extract value of parent from our array.
            parent = self.capacity[parent_index]

            # Based on the order type, we compare and swap when necessary.
            if self.order == 'min':
                if parent <= value:
                    break
                self.capacity[parent_index], self.capacity[value_at_index] = \
                    self.capacity[value_at_index], self.capacity[parent_index]
                value_at_index = parent_index

            if self.order == 'max':
                if parent >= value:
                    break
                self.capacity[parent_index], self.capacity[value_at_index] = \
                    self.capacity[value_at_index], self.capacity[parent_index]
                value_at_index = parent_index

    def delete(self):
        """
        Deletes the root element (minimum or maximum) from the heap and maintains the heap property.

        Returns:
            None
        """

        # Check if the array is full.
        self.capacity_check()

        # Last Element from the active array, in-active already deleted, just placed for a sorted purpose.
        index_last = len(self.capacity)-(self.popped+1)

        self.capacity[0], self.capacity[index_last] = self.capacity[index_last], self.capacity[0]
        self.popped += 1
        value_at_index = 0

        while value_at_index < len(self.capacity)-(self.popped+1):

            # Find Children:

            # Left Children:
            left_child_index = self._child_left(value_at_index)
            if left_child_index < len(self.capacity[:-self.popped]):
                left_child_value = self.capacity[left_child_index]
            else:
                left_child_value = None

            # Right Children:
            right_child_index = self._child_right(value_at_index)
            if right_child_index < len(self.capacity[:-self.popped]):
                right_child_value = self.capacity[right_child_index]
            else:
                right_child_value = None

            # Making Comparisons:
            if left_child_value or right_child_value:

                if self.order == 'min':
                    smaller_sibling = self._check_siblings(left_child_index,
                                                           left_child_value,
                                                           right_child_index,
                                                           right_child_value,
                                                           self.order)

                    if self.capacity[value_at_index] < self.capacity[smaller_sibling]:
                        break

                    self.capacity[value_at_index], self.capacity[smaller_sibling] =\
                        self.capacity[smaller_sibling], self.capacity[value_at_index]
                    value_at_index = smaller_sibling

                if self.order == "max":
                    greater_sibling = self._check_siblings(left_child_value,
                                                           left_child_index,
                                                           right_child_index,
                                                           right_child_value,
                                                           self.order)

                    if self.capacity[value_at_index] > self.capacity[greater_sibling]:
                        break

                    self.capacity[value_at_index], self.capacity[greater_sibling] =\
                        self.capacity[greater_sibling], self.capacity[value_at_index]
                    value_at_index = greater_sibling

            else:
                break

    def heap_sort(self):
        """
        Sorts the heap in ascending or descending order.

        Returns:
            A list containing the sorted elements of the heap.
        """
        for _ in range(len(self.capacity)):
            self.delete()

        return self.capacity[::-1]


if __name__ == "__main__":

    # Initialise an object:
    hp = Heap()

    # Insert values into our heap:
    hp.insert(5)
    hp.insert(3)
    hp.insert(4)
    hp.insert(2)
    hp.insert(6)

    # Delete:
    # hp.delete()

    print(hp.heap_sort())
    # Print our heap (array):
    print(hp)


