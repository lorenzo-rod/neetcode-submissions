# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        slow = head
        fast = head
        count = 0

        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            count += 1

        if fast.next:
            count = 2 * (count + 1)
        else:
            count = 2 * count + 1
        
        prev_node = None
        curr_node = slow.next
        slow.next = None

        while(curr_node):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        first, second = head, prev_node
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
