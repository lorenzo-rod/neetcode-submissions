# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        prev1, prev2 = ListNode(0, l1), ListNode(0, l2)
        head = l2

        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                l2.val = val % 10
                carry = val // 10
                prev1 = l1
                prev2 = l2
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                prev2.next = ListNode(0, None)
                prev2.next.val = val % 10
                carry = val // 10
                prev1 = l1
                prev2 = prev2.next
                l1 = l1.next
            elif l2:
                val = l2.val + carry
                l2.val = val % 10
                carry = val // 10
                prev1 = l1
                prev2 = l2
                l2 = l2.next
        
        if carry:
            prev2.next = ListNode(carry, None)


        return head