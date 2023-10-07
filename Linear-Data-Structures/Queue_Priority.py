# Data Structure: Priority Queue Implementation (Using Singly-Linked List)

class Node:

    def __init__(self, value, priority: int, next_=None):
        """
        Initializes a Node, with a value, priority and next reference.

        :param value (any): Any value.
        :param priority (int): An integer.
        :param next_ (Node): Reference to the next Node.
        """
        self.value = value
        self.priority = priority
        self.next = next_


class PriorityQueue:
    """
    A class to represent a Priority Queue.

    ...
    Attributes
    ----------
    head: Node
        holds the element with the highest priority.
    tail: Node
        holds the element with the least priority.

    Methods
    -------
    enqueue(value, priority: int)
        Traverse through the queue and insert the Node, where the priority is higher than the current Node's priority.
        O(n)- where n is number of Nodes in our linked list.
    deque()
        Removes an element from the start of the Queue. (O(1))
    peek(last: Boolean)
        Look at the first / last element of the Queue. (O(1))
    __str__
        :returns a string showing representing a Singly-Linked List.
    __print_helper_links(head: Node)
        A helper function for __str__().
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, value, priority: int):
        node = Node(value, priority)

        # Case 1: First Element in Queue.
        if not self.head:
            self.head = node
            self.tail = node

        # Case 2: Traversing to insert a Node, with respect to its priority.
        elif self.head:

            current_node = self.head

            while True:

                # If element being inserted has a higher priority than the current head (the highest priority).
                if node.priority > current_node.priority and current_node == self.head:
                    node.next, self.head = self.head, node
                    break

                # If element being inserted has an equal priority to the current head (the highest priority).
                elif node.priority == current_node.priority and current_node == self.head:
                    node.next, current_node.next = current_node.next, node
                    break

                # If element being inserted has a higher priority but not the highest.
                elif node.priority >= current_node.priority:
                    node.next, current_node.next = current_node.next, node
                    break

                # If element being inserted has the lowest priority in the current queue.
                if not current_node.next:
                    current_node.next, self.tail = node, node
                    break

                current_node = current_node.next

    def deque(self):

        # Case 1: No Elements
        if not self.head:
            raise IndexError("Queue is empty.")

        # Case 2: Only 1 Element in the Queue.
        elif not self.head.next:
            self.head, self.tail = None, None

        # Case 3: More than 1 Element in Queue.
        else:
            self.head = self.head.next

    def peek(self, last=False):

        # If Queue has at-least 1 element.
        if self.head:

            # Peek: Oldest Element
            if last:
                return self.tail.value

            # Peek: Latest Element
            elif not last:
                return self.head.value

        # If Queue is Empty.
        raise IndexError("Queue is empty.")

    def __str__(self):
        if not self.head:
            return "Linked List is Empty"

        return self.__str_helper(self.head)

    @staticmethod
    def __str_helper(reference: Node):

        # Base-Case:
        if not reference.next:
            return str(reference.value)

        else:
            return str(reference.value) + " -> " + PriorityQueue.__str_helper(reference.next)


if __name__ == "__main__":
    # Initialize a Queue Object.
    priority_queue = PriorityQueue()

    # Push Elements onto the Queue.
    priority_queue.enqueue("A", 1)  # A
    priority_queue.enqueue("B", 2)  # B <--> A
    priority_queue.enqueue("C", 3)  # C <--> B <--> A

    # Pop Elements from the Queue.
    priority_queue.deque()  # B <--> A

    # Peek an Element.
    print(priority_queue.peek())  # Highest Priority: B
    print(priority_queue.peek(last=True))  # Lowest Priority: A

    # Print our Queue (with Links)
    print(priority_queue)
