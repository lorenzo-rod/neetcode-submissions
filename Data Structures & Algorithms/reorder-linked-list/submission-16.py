# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = dummy = ListNode(0, head)
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        l1 = head
        l2 = prev
        prev2 = l2

        while l1:
            prev2 = l2
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2
            
        if l2:
            prev2.next = l2
        