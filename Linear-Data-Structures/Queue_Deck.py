# Data Structure: Deck / Double Ended Queue (Using Doubly-Linked List)

class Node:

    def __init__(self, value, previous_=None, next_=None):
        """
        Initializes a Node, with a value, previous reference and next reference.

        :param value (any): Any value.
        :param previous_ (Node): Reference to the previous Node.
        :param next_ (Node): Reference to the next Node.
        """
        self.value = value
        self.previous = previous_
        self.next = next_


class Deck:
    """
    A class to represent a Deck / Double Ended Queue.

    ...
    Attributes
    ----------
    head: Node
        hold the left-most element in the queue.
    tail: Node
        hold the right-most element in the queue.
    traverse: Node
        hold the current element traversed.

    Methods
    -------
    enqueue_right(value):
        To add Node(value) after the right-most element in the queue.
    enqueue_left(value):
        To add Node(value) before the left-most element in the queue.
    __enqueue(value: Any)
        A helper function that either adds the Node before and after the left-most and right-most position respectively.
    deque_right()
        To remove the right-most element in the queue.
    deque_left()
        To remove the left-most element in the queue.
    __deque(value: Any)
        A helper function that either removes the left-most or the right-most Node.
    peek(last: Boolean)
        Look at the first / last element of the Queue. (O(1))
    traversal(back: Boolean)
        Traverse the queue, like a browsing session. (O(1))
    print_links()
        :returns a string showing a Node's value, it's previous value (if any), it's next value (if any).
    __print_helper_links(head: Node)
        A helper function for print_links()
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.traverse = self.head

    def enqueue_right(self, value):
        self.__enqueue(value, enqueue="right")

    def enqueue_left(self, value):
        self.__enqueue(value, enqueue="left")

    def __enqueue(self, value, enqueue):
        node = Node(value)

        # Case 1: First Element in Queue.
        if not self.head:
            self.head = node
            self.tail = node

        elif enqueue == "right":

            # Case 2: More than 1 Element in Queue.
            if self.head:
                self.tail.previous = node
                node.previous = self.tail
                self.tail.next, self.tail = node, node

        elif enqueue == "left":

            # Case 2: More than 1 Element in Queue.
            if self.head:
                self.head.previous = node
                node.next = self.head
                self.head = node

    def deque_right(self):
        self.__deque(deque="right")

    def deque_left(self):
        self.__deque(deque="left")

    def __deque(self, deque):

        # Case 1: No Elements
        if not self.head:
            raise IndexError("Queue is empty.")

        # Case 2: Only 1 Element in the Queue.
        elif not self.head.next:
            self.head, self.tail, self.traverse = None, None, None

        elif deque == "right":
            # Case 3: More than 1 Element in Queue.
            self.tail, self.tail.next = self.tail.previous, None

        elif deque == "left":
            # Case 3: More than 1 Element in Queue.
            self.head, self.head.previous = self.head.next, None
            self.traverse = self.head

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

    def traversal(self, back=True):

        # If Queue has at-least 1 element.
        if self.head:

            # To traverse backwards / downwards (next)
            if back:
                if self.traverse.next:
                    self.traverse = self.traverse.next
                    return self.traverse.value

                return "No backwards traversals possible."

            # To traverse forwards / upwards (previous)
            if not back:
                if self.traverse.previous:
                    self.traverse = self.traverse.previous
                    return self.traverse.value

                return "No forward traversals possible."

        # If Queue is Empty.
        raise IndexError("Queue is empty.")

    def print_links(self):
        if not self.head:
            raise IndexError("Queue is empty.")

        else:
            return self.__print_helper_links(self.head)

    def __print_helper_links(self, head):

        # Base Case:
        if not head.next:
            return F"Value:({str(head.value)})" \
                   + F" Previous: {head.previous.value if head.previous else head.previous} |" \
                     F" Next: {head.next.value if head.next else head.next}"

        else:
            return F"Value:({str(head.value)})" + \
                   F" Previous: {head.previous.value if head.previous else head.previous} |" \
                   F" Next: {head.next.value} " + \
                   " <-> " + self.__print_helper_links(head.next)


if __name__ == "__main__":

    # Initialize a Queue Object.
    deck = Deck()

    # Push Elements onto the Queue.
    deck.enqueue_right("C")  # C
    deck.enqueue_right("D")  # C <--> D
    deck.enqueue_left("B")   # B <--> C <--> D
    deck.enqueue_left("A")   # A <--> B <--> C <--> D

    # Pop Elements from the Queue.
    deck.deque_right()  # A <--> B <--> C
    deck.deque_left()   # B <--> C

    # Peek at an element.
    print(deck.peek(last=True))  # C
    print(deck.peek(last=False))  # B

    # Traverse our Queue.
    print(deck.traversal(back=True))   # C (B --> C)
    print(deck.traversal(back=False))  # B (B <-- C)

    # Print our Queue (with Links)
    print(deck.print_links())
