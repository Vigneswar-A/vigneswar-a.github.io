# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def double(node):
            if not node:
                return 0
            carry, node.val = divmod(node.val*2+double(node.next), 10)
            return carry
        return ListNode(1, head) if double(head) else head
    
        