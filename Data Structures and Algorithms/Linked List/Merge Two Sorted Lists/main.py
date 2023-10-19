# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p3 = dummy

        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next

        # If there are remaining nodes in p1 or p2, attach them to the merged list.
        if p1:
            p3.next = p1
        else:
            p3.next = p2
        
        return dummy.next
