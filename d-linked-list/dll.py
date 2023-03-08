class DListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToBack(self, data):
        newNode = DListNode(data, self.tail, None)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def addToFront(self, data):
        newNode = DListNode(data, None, self.head)
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode

    def search_for_node(self, data):
        pred = None
        curr = self.head

        while curr is not None and not (data == curr.data):
            pred = curr
            curr = curr.next

        if curr is not None and (data == curr.data):
            return data


    def delete(self, data):
        pred = None
        curr = self.head

        while curr is not None and not (data == curr.data):
            pred = curr
            curr = curr.next

        if curr is not None:
            if curr == self.head:
                self.head = curr.next
            else:
                pred.next = curr.next
                curr.next = None

    def __str__(self):
        result = ''

        curr = self.head
        while curr is not None:
            result += str(curr.data) + ' '
            curr = curr.next
        return result
