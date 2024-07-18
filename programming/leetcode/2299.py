# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    
        zero = head
        head = zero
        last = zero
        sum = 0
        
        node = zero.next
        while node:
            sum += node.val
            if node.next.val == 0:
                zero.val = sum
                sum = 0
                zero.next = node.next
                last = zero
                zero = node.next
                node = node.next.next
            else:
                node = node.next

        last.next = None
        return head
                
            
            
        