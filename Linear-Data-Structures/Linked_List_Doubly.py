from Linked_List_Singly import Node, SinglyLinkedList


class NodeDLL(Node):

    def __init__(self, value, previous=None, next=None):
        super().__init__(value, next=next)
        self.previous = previous


class DoublyLinkedList(SinglyLinkedList):
    __total_nodes = 0

    def __init__(self, head: Node, tail=None):
        super().__init__(head, tail)
        DoublyLinkedList.__total_nodes += 1

    def __str__(self):
        if not self.head:
            return "Linked List is Empty"

        return self.__str_helper(self.head)

    def __str_helper(self, reference: Node):

        # Base-Case:
        if reference.next == self.head:
            return str(reference.value)

        else:
            return str(reference.value) + " <--> " + DoublyLinkedList.__str_helper(self, reference.next)

    def insert(self, node: Node, position=0):

        if position > self.__total_nodes or position < 0:
            print(F"{position} is out of bounds, would you like to append this instead ?")
            append = input("Press -1- for Yes | Press -2- for No: ")

            if append == "1":
                self.__total_nodes += 1

                # Tail (Old) <- New Node (Tail, New) -> New Node (Tail, New)
                node.previous, self.tail.next, self.tail = self.tail, node, node

                # Set self.head's previous to self.tail
                self.head.previous = self.tail

                # Set self.tail's next to self.head
                self.tail.next = self.head

            else:
                raise IndexError("Position not accessible, enter a valid position.")

        elif position == 0:
            self.__total_nodes += 1

            # New Node (new head) -> self.head (old head)
            node.next, self.head = self.head, node

            # Set self.head.previous (new head) to self.tail.previous
            self.head.previous = self.tail

            # Set self.tail.next to self.head (new head)
            self.tail.next = self.head

        elif position == 1:
            self.__total_nodes += 1
            node.previous, node.next, self.head.next = self.head, self.head.next, node

        elif position == self.__total_nodes:
            self.__total_nodes += 1

            # Tail (Old) <- New Node (Tail, New) -> New Node (Tail, New)
            node.previous, self.tail.next, self.tail = self.tail, node, node

            # Set self.head's previous to self.tail
            self.head.previous = self.tail

            # Set self.tail's next to self.head
            self.tail.next = self.head

        else:
            if (position / self.__total_nodes) > 0.5:
                self.__insert_helper(node, self.head, position, bw_traversal=True)

            else:
                self.__insert_helper(node, self.head, position)

    def __insert_helper(self, node, head, position, bw_traversal=False):

        # Base-Case:
        # Forward Traversal or Backward Traversal
        if position == 1 and not bw_traversal:
            self.__total_nodes += 1
            node.next, head.next = head.next, node
            node.previous = head

        elif bw_traversal and (self.__total_nodes - position) == -1:
            self.__total_nodes += 1
            node.previous, node.next, head = head.previous, head, node

        else:
            if bw_traversal:
                self.__insert_helper(node, head.previous, position+1, bw_traversal=True)
            else:
                self.__insert_helper(node, head.next, position-1)


dll = DoublyLinkedList(NodeDLL(1))
print(dll.tail.value)
print(len(dll))

dll.insert(Node(2), position=2)
dll.insert(Node(3))
dll.insert(Node(4))
dll.insert(Node(5))
dll.insert(Node(6))
print(dll.head.value)
print(dll.tail.value)
print(dll)
