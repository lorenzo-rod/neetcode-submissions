# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
        elif not list1:
            return list2
        else:
            return list1
        head = node
        print(node.val)
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
        return head