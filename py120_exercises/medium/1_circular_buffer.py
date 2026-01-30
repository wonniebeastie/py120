class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.next = 0
        self.oldest = 0

    def put(self, new):
        if self.buffer[self.next] is None:
            self.buffer[self.next] = new
            self.next = (self.next + 1) % self.size
        else:
            # next_index doesn't need self - it's a temporary local
            next_index = (self.next + 1) % self.size
            self.buffer[self.next] = new
            self.oldest = next_index
            self.next = next_index

    def get(self):
        # temporary local
        oldest_item = self.buffer[self.oldest]
    
        if oldest_item is None:
            return None

        self.buffer[self.oldest] = None
        self.oldest = (self.oldest + 1) % self.size
        return oldest_item

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
