# (Algorithm) - Binary Search Algorithm (Recursive Approach)

def binary_search_algorithm(array: list, value, iterations=0):
    """Perform a binary search on a sorted array to find the index of a given value.
    Time Complexity = log(n) | Space Complexity = O(1)

     Args:
         array (list): A sorted list of elements to search.
         value: The value to search for in the array.
         iterations (int, optional): The number of iterations performed in the search. Defaults to 0.

     Returns:
         tuple: A tuple containing the index of the value in the array and the number of iterations
             performed in the search. If the value is not found in the array, the index value will be -1.
     """

    # Calculations to get the middle index.
    middle_index = len(array)
    index = middle_index // 2

    # To evaluate worst-case:
    index = index if len(array) % 2 else index - 1

    # Base Case 1, Array Size recursively reduced to zero, meaning the element is not present.
    if len(array) <= 0:
        return -1, iterations

    # Base Case 2.
    elif array[index] == value:
        return index, iterations

    elif value > array[index]:
        index_, iterations_ = binary_search_algorithm(array[index + 1:], value, iterations + 1)
        return index_ + index + 1, iterations_

    elif value < array[index]:
        return binary_search_algorithm(array[:index], value, iterations + 1)


if __name__ == "__main__":
    numbers = [n for n in range(1, 11)]
    to_find = 10

    index, iterations = binary_search_algorithm(numbers, value=to_find)
    print(F"Number: {to_find} found at {index}, after {iterations} iterations.") if index > 0 else \
        print(f"{to_find} not found")
