# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        slow = head
        fast = slow
        temp = head
        
        for i in range(k):
            temp = fast
            fast = fast.next
         
        while fast:
            slow = slow.next
            fast = fast.next

        slow.val, temp.val = temp.val, slow.val
        return head
            
        