class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        found_elements = []
        while node is not None:
            if node.value == val:
                found_elements.append(node)
            node = node.next

        return found_elements

    def delete(self, val, all=False):
        node = self.head
        previous_item = None

        while node is not None and node.value == val:
            self.head = node.next
            node = None

            if all:
                node = self.head

        if self.head is None:
            self.tail = None
            return

        while node is not None:
            while node is not None and node.value != val:
                previous_item = node
                node = node.next

            if node is None:
                self.tail = previous_item
                return

            previous_item.next = node.next
            node = None
            if all:
                node = previous_item.next

        if previous_item is not None and previous_item.next is None:
            self.tail = previous_item

    def clean(self):
        node = self.head
        while node is not None:
            self.head = node.next
            node = None
            node = self.head
        self.tail = None

    def len(self):
        node = self.head
        count_of_elements = 0
        while node is not None:
            count_of_elements += 1
            node = node.next
        return count_of_elements

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

            if newNode.next is None:
                self.tail = newNode
