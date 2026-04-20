class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        node = Node(value)
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        node = self.tail.prev
        prev = node.prev

        prev.next = self.tail
        self.tail.prev = prev

        return node.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node = self.head.next
        next_node = node.next
        self.head.next = next_node
        next_node.prev = self.head

        return node.val