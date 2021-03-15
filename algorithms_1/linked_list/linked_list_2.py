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
        prev = None

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
                prev = node
                node = node.next

            if node is None:
                self.tail = prev
                return

            prev.next = node.next
            node = None
            if all:
                node = prev.next

        if prev is not None and prev.next is None:
            self.tail = prev

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
            if self.head is None:
                self.head = newNode
                newNode.prev = None
                newNode.next = None
                self.tail = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode

        if newNode.next is None:
            self.tail = newNode

    def add_in_head(self, newNode):
    	if self.head is None:
    		self.head = newNode
    		newNode.prev = None
    		newNode.next = None
    		self.tail = newNode
    	else:
    		newNode.next = self.head
    		newNode.prev = None
    	self.head = newNode
