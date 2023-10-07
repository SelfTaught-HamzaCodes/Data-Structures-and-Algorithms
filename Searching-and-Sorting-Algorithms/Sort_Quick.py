class QuickSort:
    """
    A divide-and-conquer algorithm that recursively divides an array into two sub-arrays based on a chosen pivot,
    and then sorts those sub-arrays.

    sort_quick(array: list, left, right):
        This passes an array[left:right], until left > right.
    sort_pivot(array, left, right):
        This function sorts the pivot, such that element greater than the pivot are to the right and smaller to the left

    Time Complexity:
    Best / Average:  O(log(n))
    Worst: O(n^2)

    Space Complexity:
    Worst: O(n)
    """

    @classmethod
    def sort_quick(cls, array: list, left, right):

        # Example: Array = [2, 3, 1]
        # left -> 0, right -> 3
        # This proves that we at-least have an element in our list.
        if left < right:

            # This returns a pivot index, where pivot is the sorted element.
            partition_position = cls.__sort_pivot(array, left, right)

            cls.sort_quick(array, left, partition_position-1)
            cls.sort_quick(array, partition_position+1, right)

    @staticmethod
    def __sort_pivot(array, left, right):

        i = left  # i will TRAVERSE to the RIGHT, finding a HIGHER VALUE than PIVOTS value.
        j = right - 1  # j will TRAVERSE to the LEFT, finding a LOWER VALUE than PIVOTS value.

        pivot = array[right]  # pivot will be the right most element in the given array.

        # This loop continues to run until i overlaps j, this is when we replace the i's value with pivot, and MAGIC!
        while i < j:

            # i, will traverse to the right until it finds a HIGHER VALUE than PIVOT.
            while i < right and array[i] < pivot:
                i += 1

            # j, will traverse to the left until it find a LOWER VALUE EQUAL TO than PIVOT.
            while j > left and array[j] >= pivot:
                j -= 1

            # Switch values between i and j, making i smaller than pivot and j greater than pivot, so the loop continue.
            if i < j:
                array[i], array[j] = array[j], array[i]

        # Once i surpasses j, the loop above i < j break and we check and replace i's value with pivot if:
        if array[i] > pivot:
            array[i], array[right] = array[right], array[i]

        return i


if __name__ == "__main__":
    numbers = [2, 4, 1, 5, 7, 18, 2]
    QuickSort.sort_quick(numbers, 0, len(numbers)-1)
    print(numbers)
