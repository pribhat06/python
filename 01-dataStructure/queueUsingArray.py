class Queue():
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.queue = size * [None]

    def is_empty(self):
        return (self.head == -1)
    
    def is_full(self):
        return self.head == self.size-1
    
    def enque(self, value):
        if self.is_empty():
            self.head = 0
        elif self.is_full():
            return "Overflow"
        else:
            self.head += 1


q = Queue(3)
print(q.enque(2))
