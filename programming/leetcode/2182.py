# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        min_dist = inf
        prev_crit = None
        first_crit = None
        curr = head
        i = -1
        while curr:
            i += 1
            if curr.next and curr.next.next:
                if (curr.next.val > curr.next.next.val and curr.next.val > curr.val) or (curr.next.val < curr.next.next.val and curr.next.val < curr.val):
                    if prev_crit is None:
                        first_crit = i
                    else:
                        min_dist = min(min_dist, i-prev_crit)
                    prev_crit = i
                    
            curr = curr.next
        
        return [min_dist, (prev_crit-first_crit)] if min_dist != inf else [-1, -1]