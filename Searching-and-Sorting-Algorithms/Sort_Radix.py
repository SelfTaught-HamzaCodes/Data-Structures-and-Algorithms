class RadixSort:
    """
    Radix Sort (For Positive Integers)
        A sorting algorithm that sorts elements based on their individual digits or bits.
        It first sorts elements based on the least significant digit or bit,
        and then progressively sorts them based on more significant digits or bits.

    Time Complexity
         Best / Average / Worst = N * K, where N is the number of elements and K is the highest significance of max no.

    Space Complexity
        Worst: N + K

    sort_radix(array: list):
        A function that calls __position_radix and passes the value returned to __apply_radix.

    __position_radix(array):
        A function to find the max significance, of the max integer in the array.

    __digit(number, position):
        A function that extracts the digit from the number based on the position(significance).

    __apply_radix(array, current_significance, significance):
       A function that applies the counting sort, K times. (where K is the 1 to max(significance)).

    """

    @classmethod
    def sort_radix(cls, array: list):

        # Pass the array to __position_radix to get the maximum significance.
        significance = cls.__position_radix(array)
        return cls.__apply_radix(array, current_significance=1, significance=significance)

    @staticmethod
    def __position_radix(array):

        # Example: [45, 23, 101] -> max -> 101 -> str -> '101' -> len('101') -> 3 -> Highest Significance = 3
        return len(str(max(array)))

    @staticmethod
    def __digit(number, position):

        # Example: [45, 23, 101] -> Highest Significance = 3, for (0)23, adding zero before 2 is not possible.
        # So, we convert 23 -> str and if current significance=3, '23'[-3] doesn't exist, so it means 0.
        try:
            return int(str(number)[-position])

        except IndexError:
            return 0

    @classmethod
    def __apply_radix(cls, array, current_significance, significance):

        # Base Case, as soon as the Current Significance > The Highest Significance.
        if current_significance > significance:
            return array

        # Create an array to store the counted values, where LISTS INDEX = VALUE from 0-9 and LISTS VALUE = OCCURRENCE:
        # occurrences in RADIX will always be from 0-9 as this is the limit for each Significance.
        occurrences = [0 for _ in range(10)]

        # Loop over the given array and fill the occurrences:
        # We convert the number using __digit function to extract the digit as per the current significance.
        for i in array:

            # In the occurrences array, we increment value by 1, remember LISTS INDEX = ARRAY VALUE
            digit = cls.__digit(i, position=current_significance)
            occurrences[digit] += 1

        # Once the occurrences is filled, we sum the values [2, 1] --> [2, 3], to show the repeated occurrence in order.
        for i in range(1, 10):
            occurrences[i] = occurrences[i] + occurrences[i - 1]

        # Once the occurrence are summed up, we traverse the array in reverse and fill another array.
        # Example:
        # Original   = [5, 4, 2, 2, 1, 0]
        # Occurrence = [1, 2, 4, 4, 5, 6]
        # 1st iteration, 0th number --> index in occurrence --> value --> 1 --> decrement and insert --> 0 at i=0 in New
        # Repeat
        # New = [0, 1, 2, 2, 4, 5]

        sorted_array = array[:]

        for i in range(len(array) - 1, -1, -1):

            # As per current significance, we extract the digit from the number in the array.
            current_digit = cls.__digit(array[i], current_significance)

            # Look it up in the occurrences and decrement it.
            occurrences[current_digit] -= 1

            # Insert the number, in the sorted array as per the updated occurrences list.
            sorted_array[occurrences[current_digit]] = array[i]

        # Overwriting array with the sorted_array.
        array[:] = sorted_array

        return cls.__apply_radix(array[:], current_significance + 1, significance)


if __name__ == "__main__":
    numbers = [52, 14, 22, 2, 1, 10]
    x = RadixSort.sort_radix(numbers)
    print(x)
