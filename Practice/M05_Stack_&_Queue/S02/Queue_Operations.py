#Implementation of a Queue using Linked List
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rare = None 
    def enqueue(self,val):
        new_node = Node(val)
        if self.rare is None:
            self.rare = self.front = new_node
            return 
        self.rare.next = new_node
        self.rare = new_node
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        del_val = self.front.data 
        self.front = self.front.next
        if self.front is None:
            self.rare = None 
        return del_val
    def front(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data 
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return 
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
queue = Queue_LL()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.display()
queue.dequeue()
queue.display()




