class Node:

  def __init__(self,value):

    self.data = value
    self.next = None
     

class Queue:

  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self,value):

    new_node = Node(value)

    if self.front == None:
      self.front = new_node
      self.rear = new_node

    else:
      self.rear.next = new_node
      self.rear = new_node

  def dequeue(self):

    if self.front == None:
      return "Queue empty"
    else:
      self.front = self.front.next

  def is_empty(self):
    return self.front == None

  def front_item(self):
    if (not self.is_empty()):
      return self.front.data
    else:
      return "Empty queue"

  def rear_item(self):
    if (not self.is_empty()):
      return self.rear.data
    else:
      return "Empty queue"
    

  def traverse(self):

    temp = self.front

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next


q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(7)

q.traverse()