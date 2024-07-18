# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        pointer=head
        
        while pointer:
            if pointer not in seen:
                seen.add(pointer)
            else:
                return pointer
            pointer=pointer.next
            
        return 