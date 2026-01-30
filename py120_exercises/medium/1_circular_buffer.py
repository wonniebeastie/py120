class CircularBuffer:
    """
    Initializes a buffer for each instance

    P:
    Maintain a fixed-size list that "wraps around".

    EX:
    - `buffer = CircularBuffer(3)`
        - `size` = 3
        - `buffer` = [None, None, None]
        - `next` = 0
        - `oldest` = 0
        ==> `put(1)`
            - buffer[0] = 1
            - buffer = [1, None, None]
        ==> `put(2)`
            - buffer[]
        - VISUAL:
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

    OVERVIEW:
    - `put` always writes at the "next" position
    - `get` always removes/returns the "oldest" item
    - if buffer is full, `put` overwrites the oldest
    - if buffer is empty, `get` returns `None`
    
    BRAINSTORM:
    - Need to know:
        - where to insert (index where the NEXT inserted item will go)
        - where to remove from (index of the OLDEST item)
    -----
    - use a list of fixed length `size`
    - use 2 integers:
        - `next`: index to write to next
        - `oldest`: index of item to remove next
    - use `None` to mark "empty" slots
    ----
    - use modulo % for "wrap around" behavior so we stay inside a loop of
      indices 0 ~ size-1

    METHODS:
    - `put`: Adds an object to the buffer
        ----
        I: int, new value to be added (`new`)
        O: N/A, mutates `buffer` list
        ----
        handle cases of `next` slot:
        - is empty 
        - is filled
    ====
    - `get`:
        Removes & returns the oldest object in the buffer.
        Returns `None` if buffer is empty
        ----
        I: N/A
        O: `None` or `oldest_item`
        ---
        handle cases of `oldest` slot:
        - is empty
        - is filled

    ALGO:
    - `put(new)`
        - if buffer[next] is `None`:
            - assign `new` to slot
            - set `next` to `(next + 1) % size`
        - else: (`next` slot is filled)
            - compute `next_index` by adding 1 to `next` and dividing by `size`
              to get the remainder
            - overwrite that slot with `new`
            - set `oldest` to `next_index`
            - set `next` to `next_index`

    - `get()`
        - SET `oldest_item` with buffer[oldest]
            - if `oldest_item` is `None` (means slot is empty):
                - return `None`
            - else (means slot is filled):
                - set `buffer[oldest]` to `None`
                - set `oldest` to `(oldest + 1) % size`
                - return `oldest_item`
    """
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
