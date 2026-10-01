size = 5 
li = [None] * size 
print(li)

class Circular_Queue:
    def __init__(self,size):
        self.size = size 
        self.queue = [None]*self.size
        self.front = -1
        self.rare = -1
    def enqueue(self):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data