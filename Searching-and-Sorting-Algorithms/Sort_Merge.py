class SortMerge:
    """
    MergeSort is another divide-and-conquer algorithm that recursively splits an array into two halves,
    sorts those halves, and then merges them back together.

    sort_merge_divide(array:list)
        A function that recursively splits an array until it reaches a size of 1, then passes it to the other function.
        :returns: a new list with all the values sorted.

    sort_merge_conquer(left_array: list, right_array: list)
        A helper function that uses a while loop to traverse and sort elements accordingly.

    Time Complexity:
    Best / Average / Worst: O(log(n))

    Space Complexity:
    Worst: O(n)

    Credits to: John Kwisses
    """
    @classmethod
    def sort_merge_divide(cls, array: list):

        # Base Case, keep on dividing until we reach 1 single element.
        if len(array) <= 1:
            return array

        # Devise the midpoint to split our array into two parts.
        midpoint = len(array) // 2

        # The split up arrays are then stored in left and right variables and passed to the sort_merge_conquer to sort.
        left, right = cls.sort_merge_divide(array[:midpoint]), cls.sort_merge_divide(array[midpoint:])

        return cls.__sort_merge_conquer(left_array=left, right_array=right)

    @classmethod
    def __sort_merge_conquer(cls, left_array, right_array):

        # To hold the sorted part of the array.
        sorted_array = []

        # Pointers to traverse through the semi-sorted arrays.
        left_pointer, right_pointer = 0, 0

        # Loops continues to execute unless one of the pointer is equal to the length of its respective array -1.
        while left_pointer < len(left_array) and right_pointer < len(right_array):

            # Case 1: LEFT < RIGHT, we append the LEFT and move our LEFT POINTER, as its smaller and should come first.
            if left_array[left_pointer] < right_array[right_pointer]:
                sorted_array.append(left_array[left_pointer])
                left_pointer += 1

            # Case 2: RIGHT <= LEFT, we append the RIGHT and more our RIGHT POINTER, as its smaller or equal.
            else:
                sorted_array.append(right_array[right_pointer])
                right_pointer += 1

        # Once the loop breaks we extend our Sorted Array by adding the remaining elements that couldn't be compare due
        # to an uneven distribution of length between the two arrays.
        sorted_array.extend(left_array[left_pointer:])
        sorted_array.extend(right_array[right_pointer:])

        return sorted_array


if __name__ == "__main__":
    numbers = [5, 3, 2, 6]
    x = SortMerge.sort_merge_divide(numbers)
