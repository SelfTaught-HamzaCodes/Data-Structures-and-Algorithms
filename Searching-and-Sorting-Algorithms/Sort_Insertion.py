def sort_insertion(array: list):
    """
    Insertion Sort:
    Another simple comparison-based algorithm that iterates through an array and places each element in its correct
    position relative to the elements before it.

    :param: array(list): an array that needs to be sorted.
    :return: None.

    Time Complexity:
    Best: O(n)
    Average	/ Worst: O(n^2)

    Space Complexity:
    Worst:O(1)
    """

    # Outer Loop to traverse over all the elements.
    for index in range(1, len(array)):

        # If the NEW element encountered is > than the PREVIOUS element we ignore and proceed, else:
        if array[index] < array[index - 1]:

            # Incase the NEW element is smaller, we switch it with the previous element and keep on traversing.
            # Traversing from right to left.
            for position in range(index-1, -1, -1):
                if array[position] > array[position+1]:
                    array[position+1], array[position] = array[position], array[position+1]

                # If during our traversal we encounter a greater element, we break out to avoid unnecessary
                # incrementation.
                else:
                    break


if __name__ == "__main__":
    roll_number = ["A", "C", "B"]
    sort_insertion(roll_number)
    print(roll_number)
