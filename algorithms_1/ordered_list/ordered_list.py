class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        node = self.head
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            while node is not None:
                comp = self.compare(node.value, value)
                if comp == 0:
                    self.insert(node, Node(value))
                    return
                if comp == (1 if self.__ascending else -1):
                    self.insert(node.prev, Node(value))
                    return
                if comp == (-1 if self.__ascending else 1) and node is self.tail:
                    self.insert(self.tail, Node(value))
                    return

                node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                if node is self.head and node is self.tail:
                    self.head = None
                    self.tail = None
                    return
                elif node is self.head:
                    self.head = node.next
                    self.head.prev = None
                    return
                elif node is self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                    node = self.tail
                    return
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node = node.prev
                    return
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        node = self.head
        while node is not None:
            self.head = node.next
            node = None
            node = self.head
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            newNode.next = afterNode.next
            if afterNode.next is None:
                self.tail = newNode
            else:
                afterNode.next.prev = newNode
            afterNode.next = newNode
            newNode.prev = afterNode

        if newNode.next is None:
            self.tail = newNode

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0
