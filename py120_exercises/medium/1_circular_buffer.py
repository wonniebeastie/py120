class CircularBuffer:
    """
    Initializes a buffer for each instance

    P: Maintain a fixed-size list that "wraps around".
    
    Need to know:
    - where to insert (index where the NEXT inserted item will go)
    - where to remove from (index of the OLDEST item)
    """
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.next = 0
        self.oldest = 0

    def put(self, new):
        """
        Adds an object to the buffer

        P: 
        - `put` always writes at the "next" position
        - If buffer is full, `put` overwrites the oldest
        """
        self.buffer[self.next] = new

    def get(self):
        """
        Removes & returns the oldest object in the buffer.
        Returns `None` if buffer is empty

        P: 
        -`get` always removes/returns the "oldest" item
        - If buffer is empty, `get` returns `None`
        """
        pass
"""
[0, 1, 2]

[None, None, None] empty
[1, None, None] -> None is replaced by newest (1)
[1, 2, None] -> None is replaced by newest (2)
[None, 2, None] -> oldest (1) removed, replaced by None
[None, 2, 3] -> None is replaced by newest (3)
[4, 2, 3] -> None is replaced by newest (4) - FULL
[4, None, 3] -> oldest (2) removed, replaced by None
[4, 5, 3] -> None is replaced by newest (5) - FULL
[4, 5, 6] -> oldest (3) is replaced by newest (6) - FULL
[7, 5, 6] -> oldest (4) is replaced by newest (7) - FULL
[7, None, 6] -> oldest (5) is removed, replaced by None
[7, None, None] -> oldest (6) is removed, replaced by None
[None, None, None] -> oldest (7) is removed, replaced by None
[] -> 
"""

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
