class HeapWithHeapify:
    """
    A class that implements a max heap data structure using the heapify algorithm.

    Attributes:
    -----------
    array: list
        The input array used to build the heap.

    Methods:
    --------
    _left_child_idx(parent_index: int) -> int:
        Returns the index of the left child of a given parent index.

    _right_child_idx(parent_index: int) -> int:
        Returns the index of the right child of a given parent index.

    _larger_value(left_idx: int, right_idx: int) -> int:
        Returns the index of the child with the larger value between two children indices.

    _leaf_nodes() -> int:
        Returns the number of leaf nodes in the heap.

    heapify():
        Rearranges the input array into a max heap.

    _heapify_helper(i: int, limit: int):
        A helper method for the heapify method that implements the heapify algorithm recursively.

    Time Complexity:
    ---------------
    It takes Big 0(n) time to re-order the heap, so it maintains it properties.
"""

    def __init__(self, array: list):
        """
        Constructor method that initializes the HeapWithHeapify class.

        Parameters:
        -----------
        array: list
            The input array used to build the heap.
        """
        self.array = array

    @staticmethod
    def _left_child_idx(parent_index: int) -> int:
        """
        Returns the index of the left child of a given parent index.

        Parameters:
        -----------
        parent_index: int
            The index of the parent node.

        Returns:
        --------
        int:
            The index of the left child node.
            """
        return 2 * parent_index + 1

    @staticmethod
    def _right_child_idx(parent_index: int) -> int:
        """
        Returns the index of the right child of a given parent index.

        Parameters:
        -----------
        parent_index: int
            The index of the parent node.

        Returns:
        --------
        int:
            The index of the right child node.
        """
        return 2 * parent_index + 2

    def _larger_value(self, left_idx: int, right_idx: int) -> int:
        """
        Returns the index of the child with the larger value between two children indices.

        Parameters:
        -----------
        left_idx: int
            The index of the left child node.
        right_idx: int
            The index of the right child node.

        Returns:
        --------
        int:
            The index of the child with the larger value.
        """
        # Initialise values to zero, so in-case the index is out of range it remains like this.
        # Limitations: It may not function properly when working with negative numbers.
        left_val, right_val = 0, 0

        # If left_idx within limit then update left_val.
        if left_idx < len(self.array):
            left_val = self.array[left_idx]

        # If right_idx within limit then update right_val.
        if right_idx < len(self.array):
            right_val = self.array[right_idx]

        return left_idx if left_val > right_val else right_idx

    def _leaf_nodes(self) -> int:
        """
        Returns the number of leaf nodes in the heap.

        Returns:
        --------
        int:
            The number of leaf nodes.
        """
        return len(self.array) // 2

    def heapify(self):
        """
        Rearranges the input array into a max heap.
        """

        # Get first leaf from an array.
        first_leaf = self._leaf_nodes()
        # idx will be the last parent before leaf nodes start.
        idx = first_leaf - 1

        # Get limit of our array, any index out of those will be ignored.
        limit = len(self.array) - 1

        return self._heapify_helper(idx, limit)

    def _heapify_helper(self, i: int, limit: int):
        """
        A helper method for the heapify method that implements the heapify algorithm recursively.

        Parameters:
        -----------
        i: int
            The current index of the node to be checked and, if necessary, swapped with a child node.
        limit: int
            The highest index of the array that should be considered in the heapify process.

        Returns:
        --------
        None
            The method updates the array of the HeapWithHeapify object in place.
        """

        # Base case.
        if i < 0:
            return

        # will hold the index of the largest value, so a swap can be made (if necessary).
        replacement_idx = i

        while replacement_idx <= limit:

            # Call helper methods to extract index of children and store them respectively.
            left_child_idx = self._left_child_idx(replacement_idx)
            right_child_idx = self._right_child_idx(replacement_idx)

            # If both index are out of range, then we can break out as the replacement index is already a leaf.
            if (left_child_idx, right_child_idx) > (limit, limit):
                break

            larger_child = self._larger_value(left_child_idx, right_child_idx)

            # If value at replacement_idx is greater than its children we break out.
            if self.array[replacement_idx] > self.array[larger_child]:
                break

            # Swap values.
            self.array[replacement_idx], self.array[larger_child] = \
                self.array[larger_child], self.array[replacement_idx]

            # Update replacement index.
            replacement_idx = larger_child

        # Recursive calls with i decrement by 1.
        self._heapify_helper(i - 1, limit)


if __name__ == "__main__":
    # An array of numbers:
    numbers = [5, 3, 2, 6, 4, 1, 0]

    # Initialise an object:
    hp = HeapWithHeapify(numbers)

    # Heapify once an array is initialised.
    hp.heapify()

    # Print our array, now ordered as a max-heap.
    print(hp.array)
