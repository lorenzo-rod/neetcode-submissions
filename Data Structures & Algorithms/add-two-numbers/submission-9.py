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

        while l1 and l2:
            curr.next = ListNode()
            curr = curr.next
            value = l1.val + l2.val + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            curr.val = value

            l1 = l1.next
            l2 = l2.next

        while l1:
            curr.next = ListNode()
            curr = curr.next
            value = l1.val + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            curr.val = value

            l1 = l1.next

        while l2:
            curr.next = ListNode()
            curr = curr.next
            value = l2.val + carry
            carry = value // 10
            if value >= 10:
                value -= 10
            curr.val = value

            l2 = l2.next

        while carry:
            curr.next = ListNode()
            curr = curr.next
            value = carry
            carry = value // 10
            if value >= 10:
                value -= 10
            curr.val = value

        return dummy.next
