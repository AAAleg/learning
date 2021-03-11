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
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        node = self.head
        if all:
            while node is not None:
            self.head = node.next
            node = None
            node = self.head
        else:
            if node not is None and node.value = val:
                self.head = node.next
                node = None
                return

            prev = None
            while node not is None and node.value != val:
                prev = node
                node = node.next
            if node is None:
                return
            prev.next = node.next
            node = None

    def clean(self):
        node = self.head
        while node is not None:
            self.head = node.next
            node = None
            node = self.head

    def len(self):
        node = self.head
        count = 0
        while node not is None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if not afterNode:
            newNode.next = self.head
            self.head = newNode

        newNode.next = afterNode.next
        afterNode.next = newNode
