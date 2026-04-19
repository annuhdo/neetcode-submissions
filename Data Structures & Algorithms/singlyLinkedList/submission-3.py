class LinkedList:
    
    def __init__(self):
        # dummy head so that removing a node from beginning of list is ez
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        for i in range(index):
            if curr is None:
                return -1

            curr = curr.next

        return -1 if curr is None else curr.val
        

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next
        self.head.next = new_head

        cur = self.head.next
        prev = self.head
        while cur is not None:
            prev = cur
            cur = cur.next
        self.tail = prev

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        to_delete = self.get(index)
        if to_delete is -1:
            return False

        cur = self.head
        for i in range(index):
            if cur is None:
                return False
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next

        return True
        

    def getValues(self) -> List[int]:
        new_arr = []
        cur = self.head.next
        while cur is not None:
            new_arr.append(cur.val)
            cur = cur.next

        return new_arr

        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None