size = 5 
li = [None] * size 
print(li)

class Circular_Queue:
    def __init__(self,size):
        self.size = size 
        self.queue = [None]*size
        self.front = -1
        self.rare = -1
    def enqueue(self,value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return 

        value = self.queue[self.front]
        self.queue[self.front] = None 
        if self.front == self.rare:
            self.front = -1
            self.rare = -1 
        else:
            self.front = (self.front+1) % self.size
        return value 
    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
            return 
        return self.queue[self.front]
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break 
            i = (i + 1)%self.size
        print()