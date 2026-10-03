"""Customer raffle queue using FIFO (first-in, first-out) ordering.

Customers join at the back and leave from the front. A winner is chosen
at random, then everyone from the front through that winner is dequeued.
"""

import random


class Queue:
    """A FIFO queue stored in a public Python list.

    The front of the queue is index 0, which is the first item enqueued.
    New items are appended to the back. ``self.items`` stays a list so
    callers can use ``len()``, membership tests, and printing.
    """

    def __init__(self):
        """Create an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add ``item`` to the back of the queue.

        FIFO means a later arrival waits behind everyone already in line.
        """
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        The front is the item that has been waiting the longest.

        Raises:
            IndexError: If the queue is empty, with the message
            "dequeue from empty queue".
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it.

        Returns:
            The front item, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Return True if the queue has no items, otherwise False."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """Randomly select a winner and dequeue through that customer.

        If the queue is empty, return None. Otherwise pick a random index
        with ``random.randrange`` so every customer currently in line is
        equally likely, then dequeue from the front until that winner has
        left. Customers behind the winner stay in line.

        Returns:
            The winning customer's name as a string, or None if the
            queue is empty.
        """
        if self.is_empty():
            return None

        # Random selection: every customer currently in line is equally likely.
        winner_index = random.randrange(len(self.items))
        winner = None

        # FIFO: dequeue from the front up to and including the winner so
        # earlier customers leave before the winner is announced.
        for _ in range(winner_index + 1):
            winner = self.dequeue()

        print(f"Winner: {winner}! Congratulations, you have been selected.")
        return winner


if __name__ == "__main__":
    queue = Queue()
    for number in range(1, 21):
        queue.enqueue(f"Customer #{number}")

    print(f"Front of the line (peek): {queue.peek()}")
    winner = queue.select_and_announce_winner()
    print(f"Winner returned: {winner}")
    print(f"Customers remaining: {len(queue.items)}")
    print(f"Next in line: {queue.peek()}")
