'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1=Node(10)
node2=Node(20)
node3=Node(40)
node4=Node(50)
node1.next=node2
node2.next=node3
node3.next=node4
def traverse():
    curr=node1
    while curr:
        print(curr.data,end= " -> ")
        curr=curr.next
    print("None")
traverse()
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def insert_at_pos(head, data, pos):
    new_node = Node(data)
    if pos == 0:
        new_node.next = head
        return new_node
    curr = head
    for _ in range(pos - 1):
        if curr is None:
            raise IndexError("Position out of bounds")
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head 
def delection_begin(head):
    if head is None:
        print("Error")
    now_head = head.next
    del head
    return new_head 

def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" -> ")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head, 10)
head=insert_begin(head, 20)
head=insert_begin(head, 30)
print("Insertion at beginning:")
traverse(head)
print(head)

head=insert_end(head, 40)
head=insert_end(head, 50)
print("Insertion at end:")
traverse(head)

head=insert_at_pos(head, 25, 2)
print("Insertion at position 2:")   
traverse(head)

print("Delection at the beginning :")
head = delection_begin(head)
traverse(head)
print()
