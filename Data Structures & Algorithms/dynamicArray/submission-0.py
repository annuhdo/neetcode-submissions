class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if (self.length >= self.capacity):
            self.resize()

        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.getSize() <= 0:
            return -1

        self.length -= 1
        res = self.arr[self.length]

        return res
 

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(0, self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity

