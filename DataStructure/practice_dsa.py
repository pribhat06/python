
print("*****************************")

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size-1:
            return "Overflow!"
        else:
            self.top +=1
            self.stack[self.top] = value
            return f"value: {value}, self.stack : {self.stack}"
        
    def pop(self):
        if self.top == -1:
            return "Empty Stack"
        else:
            ret = f" ret self.top : {self.stack[self.top]}"
            self.top -= 1
            return f"ret : {ret}, self.top: {self.top}, self.stack[self.top] : {self.stack[self.top]}"
        
    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i], end= " ")

        
    

s = Stack(3)
print(s.push(3))
print(s.push(5))
print(s.push(7))
print(s.push(9))

print(s.pop())
s.traverse()


print("***************QUEUE**********************")

class Queue():
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.queue = [None] * size


    def is_empty(self):
        return (self.head == -1)

    def is_full(self):
        return (self.head == self.size-1 )

    def enque(self, value):
        if self.is_empty():
            self.head = 0
        elif self.is_full():
            return "!! overflow"
        else:
            self.head += 1
            self.queue[self.head] = value






q = Queue(3)
print(q.enque(4))