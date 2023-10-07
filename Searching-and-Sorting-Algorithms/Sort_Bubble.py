def sort_bubble(array: list):
    """
    A simple comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order.

    :param: array(list): an array that needs to be sorted.
    :return: array(list): a sorted array, changes the original array.

    Time Complexity:
    Best: O(n)
    Average / Worst: O(n^2)

    Space Complexity:
    Worst: O(1), Inplace sorting algorithm.
    """

    # Raise an assertion error in the case the correct type for parameter array is not provided.
    assert isinstance(array, list), "Pass in an array to sort."

    # Iterative Method:
    unsorted_elements = len(array)

    while unsorted_elements > 0:
        for index in range(unsorted_elements):

            # Last element reached in the list, no elements left to be compared.
            if index == unsorted_elements - 1:
                unsorted_elements -= 1
                break

            # Switch Positions, if current element is greater than next element
            elif array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

    return array

if __name__ == "__main__":
    numbers = [1, 3, 2, 1]
    sort_bubble(numbers)
    print(numbers)
