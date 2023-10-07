class HashTable:
    """
    Implementation of a Hash Table:
        Hash Function: Multiplication Method.
        Hashing: Double-Hashing.
    """

    # Size of our array to hold values.
    __size = 10

    def __init__(self, size=0):

        if size:
            self.array = [()] * size
            self.__size = size
            return

        self.array = [()] * HashTable.__size

    def __getitem__(self, key):

        hash_value, retrieve = self.__get_hash_value(key)

        # var:retrieve, will contain a tuple (key, value).
        if retrieve[0] == key:
            return retrieve[1]

        self.__double_hashing(hash_value, key, state="get")

    # noinspection PyTypeChecker
    def __setitem__(self, key, value):

        hash_value, retrieve = self.__get_hash_value(key)

        # Currently, Empty:
        if not retrieve:
            self.array[hash_value] = (key, value)
            return

        self.__double_hashing(hash_value, key, value, state="set")

    def __delitem__(self, key):

        hash_value, retrieve = self.__get_hash_value(key)

        # No Key:
        if not retrieve:
            raise KeyError(key)

        # Key Found, on the same place as produced by the Hash-Function.
        elif retrieve[0] == key:
            self.array[hash_value] = ()
            return

        self.__double_hashing(hash_value, key, state="del")

    def __multiplication_method(self, key, num_parts):

        digits = len(str(self.__size)) // 2

        if isinstance(key, (int, float)):

            # Convert the key to a string
            key_str = str(key)

            # Divide the key into equal-sized parts
            parts = [int(key_str[i:i + num_parts]) for i in range(0, len(key_str), num_parts)]

            # Compute the sum of the parts
            hash_val = sum(parts)

            # Take the modulus of the sum with the table size
            hash_val %= self.__size

            return hash_val

        if isinstance(key, str):
            hash_value = 0

            for char in str(key):
                hash_value += ord(char)

            return hash_value % HashTable.__size

    def __double_hashing(self, hash_value, key, value=None, state=None):

        # Breakdown: array_size = (hash_value + 1) % self.__size
        # Array Size: 4, currently at:
        # Iteration 1: 2 % 4 -> 2 (Start)
        # Iteration 2: 3 % 4 -> 3,
        # Iteration 3: 4 % 4 -> 0,
        # Iteration 4: 5 % 4 -> 1 (Break)

        for i in range(len(self.array) - 1):
            array_size = (hash_value + i**2) % self.__size

            if not self.array[array_size]:
                self.array[array_size] = (key, value)
                return

            if self.array[array_size][0] == key:
                if state == "del":
                    self.array[array_size] = ()
                    return

                elif state == "get":
                    return self.array[array_size][1]

                else:
                    self.array[array_size] = (key, value)

            hash_value += 1

        else:
            raise IndexError("Array is full.") if state == "set" else KeyError(key)

    def __get_hash_value(self, key):

        # Calculate Hash Value:
        hash_value = self.__multiplication_method(key, 2)

        # As per the calculated value retrieve the key:
        retrieve = self.array[hash_value]

        return hash_value, retrieve

    def print_table(self):
        print(self.array)


if __name__ == "__main__":
    # Initialise a Hash Table Function:
    ht = HashTable()

    # Setting an Item, ht[key] = value.
    ht[1] = "January"
    ht[2] = "February"
    ht[3] = "March"
    ht[4] = "April"
    ht[5] = "May"
    ht[6] = "June"
    ht[7] = "July"
    ht[8] = "August"
    ht[9] = "September"
    ht[10] = "October"

    # Getting an (Existing) Item, ht[key].
    print(ht[1])

    # Deleting an (Existing) Item, del ht[key].
    del ht[1]

    # Print our Array, with (Key & Value)
    ht.print_table()

    # Getting an (Non-existing) Item, ht[key], will raise an exception.
    # print(ht["Hamza"])

    # Deleting an (Non-existing) Item, del ht[key], will raise an exception.
    # del(ht[11])
