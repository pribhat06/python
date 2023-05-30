class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            return f'!! ERROR - OVERFLOW --> top: {self.top}, size: {self.size}'
        else:
            self.top += 1
            self.stack[self.top] = value
            return f'PUSHED --> top: {self.top}, value: {value}, size: {self.size}'

    def pop(self):
        if self.top == -1:
            return f'!! ERROR - EMPTY STACK --> top: {self.top}, size: {self.size}'
        else:
            ret = f'POPPED --> top: {self.top}, value: {self.stack[self.top]}, size: {self.size}'
            data = self.stack[self.top]
            self.top -= 1
            return ret

    def traverse(self):
        for i in range(self.top+1):
            print(self.stack[i], end = ' ')

    def peek(self):
        pass


    
s = Stack(3)  

print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.push(7))
print(s.push(8))
      
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.push(22))
print(s.push(33))
print(s.push(44))
print(s.push(55))

s.traverse()

print(s.peek())


    

