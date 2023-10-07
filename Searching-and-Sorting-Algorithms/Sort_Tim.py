class TimSort:
    """
    Timsort:
    A hybrid sorting algorithm that combines elements of merge sort and insertion sort.
    It first divides the array into small sub-arrays,
    sorts them using insertion sort,
    and then merges those sub-arrays using merge sort.

    sort_merge_divide(array:list)
        A function that recursively splits an array until it reaches a size of 1, then passes it to the other function.
        :returns: a new list with all the values sorted.

     __insertion_sort(left_array: list, right_array: list)
        A helper function that uses insertion sort to sort the sub-array and return the array.

    Time Complexity:
    Best: O(n)
    Average / Worst: O(log(n))

    Space Complexity:
    Worst: O(n)
    """
    @classmethod
    def tim_divide(cls, array: list):

        # Base Case, keep on dividing until we reach 1 single element.
        if len(array) <= 1:
            return array

        # Devise the midpoint to split our array into two parts.
        midpoint = len(array) // 2

        # The split up arrays are then stored in left and right variables and passed to the __insertion_sort to sort.
        left, right = cls.tim_divide(array[:midpoint]), cls.tim_divide(array[midpoint:])

        return cls.__insertion_sort(left_array=left, right_array=right)

    @classmethod
    def __insertion_sort(cls, left_array, right_array):

        array = left_array + right_array

        # Outer Loop to traverse over all the elements.
        for index in range(1, len(array)):

            # If the NEW element encountered is > than the PREVIOUS element we ignore and proceed, else:
            if array[index] < array[index - 1]:

                # Incase the NEW element is smaller, we switch it with the previous element and keep on traversing.
                # Traversing from right to left.
                for position in range(index - 1, -1, -1):
                    if array[position] > array[position + 1]:
                        array[position + 1], array[position] = array[position], array[position + 1]

                    # If during our traversal we encounter a greater element, we break out to avoid unnecessary
                    # incrementation.
                    else:
                        break

        return array


if __name__ == "__main__":
    numbers = [5, 3, 2, 6]
    x = TimSort.tim_divide(numbers)
    print(x)