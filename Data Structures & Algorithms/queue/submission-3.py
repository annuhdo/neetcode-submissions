class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.next.prev = new_node

        self.head.next = new_node
        new_node.prev = self.head
        

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1

        to_remove = self.tail.prev
        previous = to_remove.prev
        previous.next = self.tail
        self.tail.prev = previous

        return to_remove.val
        

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1

        to_remove = self.head.next
        next_node = to_remove.next
        self.head.next = next_node
        next_node.prev = self.head
        
        return to_remove.val
