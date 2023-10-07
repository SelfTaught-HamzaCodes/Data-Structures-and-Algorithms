class HashMap:
    """
    A Hash Map, also known as a hash table.
        Is a data structure that stores key-value pairs.
        It uses a hash function to map each key to an index in an array, where the corresponding value is stored.

    Types of Hash Functions:

        - Division Method: Value of k is divided by M and uses the remainder as obtained.
            Formula: h(k) = k mod M (where k=key value and M = the size of the hast table)
                Advantages: Works on any value of M and extremely quick as one operation is done.
                Disadvantages: Poor performance as consecutive keys are mapped to consecutive hash values, M requires caution.
                    Example: k = 1320, M = 11, h(1320) = 1320 mod 11, 0

        - Mid Square Method:
            Step 1: Squaring the value of k (like k*k)
            Step 2: Extract the hash value from the middle r digits
                Formula: h(K) = h(k * k) (where k=key value)
                    Advantages: All values of a key participate, top or bottom values don't contribute to the hashed value.
                    Disadvantages: If key is large, squaring it will be twice as many digits, resulting in repeated collisions.
                        Example: k = 50, k = 50*50 = 2500, 2-50-0

        - Folding Method:
            Step 1: Divide key value into equal parts, with exception possible for the last value can be fewer.
            Step 2: Add each component separately.
                Formula: s = k1 + k2 + k3 ... kn  --> h(K) = s  (where, s=addition of the parts of key K)
                    Advantages: Breaks key value for any easy hash value, also independent of distribution in Hash Table.
                    Disadvantages: Inefficient if too many collisions.
                        Example: k=54321, k1= 54 k2=32 k1=1, s = k1 + k2 + k3, 54 + 32 + 1 = 87

        - Multiplication Method:
            Step 1: Pick up a constant value A (where O < A < 1).
            Step 2: Multiply A with the key value.
            Step 3: Take the fractional part of kA.
            Step 4: Take the result of the previous step and multiply it by the size of the hash table, M.
                Formula: h(K) = floor(M (kA mod 1)), where M = size of the hash table, K = key value and A = constant value.
                    Advantages: It may be applied to any number between 0 and 1.
                    Disadvantages: When the table size is a power of two then this is quicker.
                        Example: k=1234, A= 0.35784, M=100, h(1234) = floor [100(1234 X 0.35784 mod 1)] = floor [57.456]

        - Choosing a good hash function:
            Creating an effective hash function that distributes the added item's index value evenly across the database is important.
            Quick and easier to compute according to the requirements.
            An approach to successfully resolve collisions in hash tables is essential for generating an index for a key whose hash index corresponds to an existing spot.

    Time Complexity:
        Search, Insert, Delete
            Best / Average: O(1).
            Worst: O(n).

    Space Complexity:
        Worst: O(n)

    """

    # Hash-table size:
    size = 10

    def __init__(self):
        self.array = [None] * HashMap.size
        self.track = {}  # For Open-Hashing.

    def __getitem__(self, key):
        hv = self.track[key]

        return self.array[hv]

    def __setitem__(self, key, value):
        hv = self.__hash_value(key)

        # Open Hashing: Finds the next available spot, if the generated hash value is already occupied.
        if self.array[hv] is not None:
            counter = hv

            while True:
                counter = (counter + 1) % HashMap.size

                if self.array[counter] is None:
                    self.track[key] = counter
                    self.array[counter] = value
                    break

                if counter == hv:
                    raise IndexError("Hash Map (Hash Table) is full")

        else:
            self.track[key] = hv
            self.array[hv] = value

    @staticmethod
    def __hash_value(key):
        hv = 0

        for char in key:
            hv += ord(char)

        return hv % HashMap.size

    def print_table(self):
        print(self.array)


if __name__ == "__main__":

    # Create hash-table instance:
    ht = HashMap()

    # Add values to hash-table:
    ht["Harry"] = "Gamer"
    ht["Helen"] = "Developer"
    ht["Adam"] = "Electronics Specialist"
    ht["Nautilus"] = "Web Developer"
    ht["Uri"] = "Sports Expert"

    # Get Value:
    print(F"Harry is a {ht['Harry']}.")
    print(F"Helen is a {ht['Helen']}.")
    print(F"Adam is a {ht['Adam']}.")
    print(F"Nautilus is a {ht['Nautilus']}.")
    print(F"Uri is a {ht['Uri']}.")

    # Print Hash Table:
    ht.print_table()  # None represent `empty` space in our Hash Table.
