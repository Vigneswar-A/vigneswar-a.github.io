# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next
        queue = []
        
        while curr:
            if curr.val >= x:
                queue.append(curr)
                prev.next = curr.next
                curr = prev.next
            
            else:
                prev = curr
                curr = prev.next
              
        for node in queue:
            prev.next = node
            prev = prev.next
            
        prev.next = None
        return dummy.next
                
        