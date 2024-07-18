# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        res = []
        stack = []
        idx = 0
        currnode = head
        
        while currnode:
            while stack and currnode.val > stack[-1][1]:
                pidx, _ = stack.pop()
                res.append((pidx, currnode.val))
            stack.append((idx, currnode.val))
            currnode = currnode.next
            idx += 1
            
        while stack:
            pidx, _ = stack.pop()
            res.append((pidx, 0))
            
        return [g for i,g in sorted(res)]
        