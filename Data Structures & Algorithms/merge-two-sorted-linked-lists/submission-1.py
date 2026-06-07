# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        head = node
        while(list1 or list2):
            if (list1 and list2 and list1.val < list2.val):
                node.next = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                node.next = ListNode(list1.val)
                list1 = list1.next
            node = node.next
        return head.next