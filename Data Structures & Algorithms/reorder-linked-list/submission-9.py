# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        fast = slow = head
        prev = None

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        prev.next = None
        prev, curr = None, slow

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        list1, list2 = head, prev
        
        while list1:
            prev2 = list2
            tmp1 = list1.next
            tmp2 = list2.next
            list1.next = list2
            list2.next = tmp1
            list1 = tmp1
            list2 = tmp2
        
        if list2:
            prev2.next = list2
