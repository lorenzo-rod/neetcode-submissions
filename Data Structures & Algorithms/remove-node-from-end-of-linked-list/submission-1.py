# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        arr = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr[-n] = "#"

        dummy = curr = ListNode()

        for val in arr:
            if val == "#":
                continue
            curr.next = ListNode(val, None)
            curr = curr.next
        
        return dummy.next