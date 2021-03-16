class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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

        while node is not None:
            if node.value == val:
                if node is self.head and node is self.tail:
                    self.head = None
                    self.tail = None
                elif node is self.head:
                    self.head = node.next
                    self.head.prev = None
                elif node is self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                    node = self.tail
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node = node.prev
                if all is False:
                    return
            node = node.next

    def clean(self):
        node = self.head
        while node is not None:
            self.head = node.next
            node = None
            node = self.head
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode

        if newNode.next is None:
            self.tail = newNode

    def add_in_head(self, newNode):
        if self.head is not None:
            newNode.next = self.head
            newNode.next.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
            
