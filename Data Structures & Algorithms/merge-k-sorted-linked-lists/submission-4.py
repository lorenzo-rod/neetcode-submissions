# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for node_list in lists:
            
            while node_list:
                arr.append(node_list.val)
                node_list = node_list.next
        
        arr.sort()

        dummy = curr = ListNode()

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next