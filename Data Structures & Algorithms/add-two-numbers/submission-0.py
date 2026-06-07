# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = l1
        node2 = l2

        last = l1
        prev1 = None

        reminder = 0
        while(node1 and node2):
            val = node1.val + node2.val + reminder
            reminder = int(val / 10)
            val = val % 10
            node1.val = val
            prev1 = node1
            last = node1
            node1 = node1.next
            node2 = node2.next

        while(node1):
            val = node1.val + reminder
            reminder = int(val / 10)
            val = val % 10
            node1.val = val
            last = node1
            node1 = node1.next

        if node2:
            prev1.next = node2
        
        while(node2):
            val = node2.val + reminder
            reminder = int(val / 10)
            val = val % 10
            node2.val = val
            last = node2
            node2 = node2.next
        
        if reminder:
            last.next = ListNode(reminder)
        
        return l1

        
