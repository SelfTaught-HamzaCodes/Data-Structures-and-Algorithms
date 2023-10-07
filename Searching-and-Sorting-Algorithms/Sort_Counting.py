class CountingSort:
    """
    Counting Sort:
        A non-comparison-based sorting algorithm that counts the number of occurrences of each element in an array,
        and then uses those counts to place each element in its correct position in a sorted array.

    Time Complexity:
        Best / Average / Worst: N + K,
        where N is the number of elements and K is the range of elements (min-max)

    Space Complexity:
        Worst: N

    Drawbacks:
    - Cannot sort non-integer values (including negative integers)
    - In-efficient when an outlier is present in our array.

    sort_counting(array: list):
        An array that needs to be sorted.
        Sorts the arrays passed, thus returns None.
    """

    @classmethod
    def sort_counting(cls, array: list):
        """
        Sorts the given array using the counting sort algorithm.

        Parameters:
        - array (list): An array of integers to be sorted.

        Returns:
        - None: The method sorts the input array in place and does not return a value.
        """
        # Finding Range (K):
        # Example: [5, 4, 2, 2, 1, 0], max=5
        maximum = max(array)

        # Create an array to store the counted values, where LISTS INDEX = VALUE and LISTS VALUE = OCCURRENCE:
        occurrences = [0 for _ in range(maximum+1)]

        # Loop over the given array and fill the occurrences:
        #           0  1  2  3  4  5
        # Example: [1, 1, 2, 0, 1, 1]
        for i in array:

            # In the occurrences array, we increment value by 1, remember LISTS INDEX = ARRAY VALUE
            occurrences[i] += 1

        # Once the occurrences is filled, we sum the values [2, 1] --> [2, 3], to show the repeated occurrence in order.
        #           0  1  2  3  4  5
        # Example: [1, 2, 4, 4, 5, 6], where 6 the last element is length of array.
        for i in range(1, maximum+1):
            occurrences[i] = occurrences[i] + occurrences[i-1]

        # Once the occurrence are summed up, we traverse the array in reverse and fill another array.
        # Example:
        # Original   = [5, 4, 2, 2, 1, 0]
        # Occurrence = [1, 2, 4, 4, 5, 6]
        # 1st iteration, 0th number --> index in occurrence --> value --> 1 --> decrement and insert --> 0 at i=0 in New
        # Repeat
        # New = [0, 1, 2, 2, 4, 5]

        sorted_array = array[:]

        for i in range(len(array)-1, -1, -1):
            occurrences[array[i]] -= 1
            sorted_array[occurrences[array[i]]] = array[i]

        # Overwriting array with the sorted_array.
        array[:] = sorted_array


if __name__ == "__main__":
    numbers = [5, 4, 2, 2, 1, 0]
    CountingSort.sort_counting(numbers)
    print(numbers)

