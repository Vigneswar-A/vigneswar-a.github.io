# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        curr = head

        while curr:
            while stack and curr.val > stack[-1].val:
                stack.pop()
            if curr:
                stack.append(curr)
                curr = curr.next

        head = curr = ListNode()
        for i in stack:
            curr.next = i
            curr = i
            
        return head.next
            
