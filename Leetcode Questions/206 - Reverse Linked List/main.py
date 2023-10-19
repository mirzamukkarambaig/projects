# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head
        
        # Recursively reverse the remaining list
        reversed_list = self.reverseList(head.next)
        
        # Connect the next node's next pointer to the current node
        head.next.next = head
        
        # Disconnect the current node's next pointer
        head.next = None

        return reversed_list
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head
        
        # Recursively reverse the remaining list
        reversed_list = self.reverseList(head.next)
        
        # Connect the next node's next pointer to the current node
        head.next.next = head
        
        # Disconnect the current node's next pointer
        head.next = None

        return reversed_list
        