# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = curr = ListNode(0, head)

        for _ in range(n):
            curr = curr.next
        
        skip = dummy

        while curr:
            curr = curr.next
            skip = skip.next
        
        curr = dummy

        while curr:
            if curr.next == skip:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
        
        return dummy.next
        
