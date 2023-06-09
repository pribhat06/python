class Stack():
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None] * 3

    def push(self, value):
        if self.top == self.size-1:
            return f"!! Overflow !!"
        else:
            self.top += 1
            self.stack[self.top] = value
            return f"self.top : {self.top}, self.size : {self.size},self.stack[self.top] {self.stack[self.top]} , value {value} self.stack : {self.stack}"

    def pop(self):
        if self.top == -1:
            return f"!! Stack is EMPTY !!"
        else:
            self.stack[self.top]
            self.top -= 1
            return f"self.stack[self.top] : {self.stack[self.top]}"
        
    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i], end = '')


s = Stack(3)
print(s.push(51))
print(s.push(54))
print(s.push(58))
print(s.push(68))

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.traverse())
    
        

print("***********************")

class Queue():
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = -1
        self.queue = [None] * size

    def enqueue(self, value):
        if self.tail == -1:
            self.tail = 0
            return "queue is EMPTY"
        elif self.tail == self.size-1:
            return f"!! Overflow , self.size{self.size}!!"
        else:
            self.tail += 1
            self.queue[self.tail] = value
            return f" Enque state, self.queue: {self.queue} || self.tail {self.tail}, self.head {self.head}"


q = Queue(3)
print(q.enqueue(51))