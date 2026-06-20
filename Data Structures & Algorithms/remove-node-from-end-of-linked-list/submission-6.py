# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode = ListNode(0, head)
        left, curr = dummynode, head

        for _ in range(n):
            curr = curr.next

        right = curr

        while right:
            left = left.next
            right = right.next
        
        curr = dummynode

        while True:
            if curr != left:
                curr = curr.next
            else:
                curr.next = curr.next.next
                break

        return dummynode.next
