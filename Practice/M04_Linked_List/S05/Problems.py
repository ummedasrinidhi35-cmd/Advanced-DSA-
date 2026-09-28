#Middle of the Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#solution 1
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid_ind = count // 2
        temp = head
        for i in range(mid_ind):
            temp = temp.next
        return temp
#solution 2
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.middleNode(head)
print(result.val) 
# Definition for singly-linked list.141
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#solution1
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        temp = head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False
#solution2
class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
        return False
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)


head.next.next.next.next = head.next

solution = Solution()
print(solution.hasCycle(head))
#21  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp = ListNode()
        curr = temp
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return temp.next

        
        