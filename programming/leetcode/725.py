# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        arr = []
        while head:
            arr.append(head)
            head = head.next
            
        size, extras = divmod(len(arr), k)
        if len(arr) <= k:
            for node in arr:
                node.next = None
            return arr + [None] * (k-len(arr))
        res = []
        prev = 0
        i = size-1
        while i < len(arr):
            if extras:
                i += 1
                extras -= 1
            arr[i].next = None
            res.append(arr[prev])
            prev = i+1
            i += size
        return res
                
        