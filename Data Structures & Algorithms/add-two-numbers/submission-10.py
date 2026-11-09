# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            curr.val = value

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
