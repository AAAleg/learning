from deque import Deque


def is_palindrome(string):
    deque = Deque()
    for symbol in string:
        deque.addFront(symbol)

    while not deque.isEmpty():
        tail = deque.removeTail()
        head = deque.removeFront()

        if head != tail and head is not None:
            return False

    return True
