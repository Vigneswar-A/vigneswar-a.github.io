# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        pointer=res
        extra=0
        while l1 or l2:
            extra,sum_=divmod((l1 and l1.val or 0)+(l2 and l2.val or 0)+extra,10)
            pointer.next=ListNode(sum_)
            l1,pointer,l2=l1 and l1.next,pointer.next,l2 and l2.next
        
        if extra:
            pointer.next=ListNode(extra)
         
        return res.next
            
        
        
        
        