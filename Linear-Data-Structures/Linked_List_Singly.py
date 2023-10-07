class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    """
    Singly-Linked List

    This is an implementation of a Singly-Linked List in Python.

    A recursive approach has been used for most methods, for practice reasons.

    Methods of Singly-Linked List:
    1- insert(node, position)
    2- print() (__str__)
    3- len()
    4- count()
    5- for loop (__iter__)
    6- delete(position)
    7- sort()
    8- reverse()
    9- Python List to Singly-Linked List
    """

    __total_nodes = 0

    def __init__(self, head: Node, tail=None):
        self.head = head
        self.tail = self.head
        self.__total_nodes += 1

    def __str__(self):
        if not self.head:
            return "Linked List is Empty"

        return self.__str_helper(self.head)

    def __len__(self):
        return self.__total_nodes

    def __iter__(self):

        current_node = self.head

        while current_node:
            yield current_node.value
            current_node = current_node.next

    def count(self, value):

        current = self.head
        counter = 0
        while current:
            if current.value == value:
                counter += 1
            current = current.next
        return counter

    @staticmethod
    def __str_helper(reference: Node):

        # Base-Case:
        if not reference.next:
            return str(reference.value)

        else:
            return str(reference.value) + " -> " + SinglyLinkedList.__str_helper(reference.next)

    # insert by default always insert as head, position > total_nodes insert at end after prompt.
    def insert(self, node: Node, position=0):

        if position > self.__total_nodes or position < 0:
            print(F"{position} is out of bounds, would you like to append this instead ?")
            append = input("Press -1- for Yes | Press -2- for No: ")

            if append == "1":
                self.__total_nodes += 1
                self.tail.next, self.tail = node, node

            else:
                raise IndexError("Position not accessible, enter a valid position.")

        elif position == 0:
            self.__total_nodes += 1
            node.next, self.head = self.head, node

        elif position == 1:
            self.__total_nodes += 1
            node.next, self.head.next = self.head.next, node

            if self.__total_nodes < 3:
                self.tail = node

        elif position == self.__total_nodes:
            self.__total_nodes += 1
            self.tail.next, self.tail = node, node

        else:
            self.__insert_helper(node, self.head, position)

    def __insert_helper(self, node, head, position):

        # Base-Case:
        if position == 1:
            self.__total_nodes += 1
            node.next, head.next = head.next, node
            if not node.next:
                self.tail = node

        else:
            self.__insert_helper(node, head.next, position - 1)

    # insert by default always insert as head, position > total_nodes insert at end after prompt.
    def delete(self, position=0):

        # If linked-list is empty
        if not self.head:
            return "Linked List is Empty."

        if position > self.__total_nodes or position < 0:
            print(F"{position} is out of bounds, would you like to pop / dequeue this instead ?")
            pop_dequeue = input("Press -1- for Yes | Press -2- for No: ")

            if pop_dequeue == "1":
                self.__total_nodes -= 1
                if not self.head.next:
                    self.tail = None
                self.head = self.head.next

        elif position == 0:
            self.__total_nodes -= 1
            if not self.head.next:
                self.tail = None
            self.head = self.head.next

        elif position == 1:
            self.__total_nodes -= 1
            if not self.head.next:
                self.tail = None
            self.head.next = self.head.next.next

        elif position == self.__total_nodes:
            self.__total_nodes -= 1
            if not self.head.next:
                self.head = self.tail = None
            else:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None
                self.tail = current

        else:
            self.__delete_helper(self.head, position)

    def __delete_helper(self, head, position):

        # Base-Case:
        if position == 1:
            self.__total_nodes -= 1
            head.next = head.next.next

        else:
            self.__delete_helper(head.next, position - 1)

    def list_to_linked_list(self, list_to_nodes):
        self.__l_to_ll_helper(list_to_nodes, index=0)

    def __l_to_ll_helper(self, list_to_nodes, index):

        # Base-Case:
        if index == len(list_to_nodes):
            return

        self.insert(Node(list_to_nodes[index]), position=index)
        self.__l_to_ll_helper(list_to_nodes, index + 1)

    def sort_selection(self, head=1):

        if head == 1:
            head = self.head

        # Base-Case:
        if not head:
            return

        else:
            index = self.__sort_selection_helper(index=head,
                                                 minimum_value=head,
                                                 current_value=head)

            self.sort_selection(head=index)

    def reverse_selection(self, head=1):

        if head == 1:
            head = self.head

        # Base-Case:
        if not head:
            return

        else:
            index = self.__sort_selection_helper(index=head,
                                                 minimum_value=head,
                                                 current_value=head,
                                                 reverse=True)

            self.reverse_selection(head=index)

    def __sort_selection_helper(self, index, minimum_value, current_value, reverse=False):

        if reverse:
            if current_value.value > minimum_value.value:
                minimum_value = current_value

        else:
            if current_value.value < minimum_value.value:
                minimum_value = current_value

        # Base-Case:
        if not current_value.next:
            index.value, minimum_value.value = minimum_value.value, index.value
            return index.next

        return self.__sort_selection_helper(index, minimum_value, current_value.next, reverse=reverse)


if __name__ == "__main__":

    # Initialise a Node.
    node_1 = Node(1)

    # Initialise a Singly-Linked List.
    sll = SinglyLinkedList(node_1)

    # Insert(), Singly-Linked List.
    sll.insert(Node(2))  # At position 0.
    sll.insert(Node(3), position=1)  # At position 1.
    sll.insert(Node(2), position=3)  # At last-position available.

    # Instance Attributes.
    print("Head: ", sll.head.value)
    print("Tail: ", sll.tail.value)

    # Print(), Singly-Linked List.
    print(sll)

    # Len(), Length of Singly-Linked List.
    print(len(sll))

    # Iter(), Iterate over Singly-Linked List.
    for index_, value_ in enumerate(sll):
        print(F"Index: {index_}", F"Value: {value_}")

    # Count(), Count an element in Singly-Linked List.
    print(sll.count(2))

    # Delete(), Singly-Linked List.
    sll.delete()  # Delete at position 0.
    sll.delete(position=2)  # Delete at position 2.
    print(sll)
    sll.delete()
    sll.delete()
    print(sll)

    # Python List -> Singly-Linked List
    numbers = [1, 4, 2, 5, 8]
    sll.list_to_linked_list(numbers)
    print(sll)

    # Sort() - Using Selection Sort.
    sll.sort_selection()
    print("Sorted (Ascending): ", sll)

    # Reverse() - Using Selection Sort.
    sll2 = SinglyLinkedList(Node(1))
    sll2.delete()
    sll2.list_to_linked_list(numbers)

    sll2.reverse_selection()
    print("Reversed (Descending): ", sll2)
