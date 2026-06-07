# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        fast = head

        while(fast.next and fast.next.next):
            fast = fast.next.next
            length += 1
        
        if fast.next:
            length = 2 * (length + 1)
        else:
            length = 2 * length + 1
        
        index = length - n - 1

        if index == -1:
            return head.next

        count = 0
        node = head

        while(node):
            if (count == index):
                node.next = node.next.next
                return head
            count += 1
            node = node.next
        return head



