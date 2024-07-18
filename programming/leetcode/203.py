# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:return
        dummy=ListNode(next=head)
        pointer=dummy
        while pointer.next:
            if pointer.next.val==val:
                pointer.next=pointer.next.next
                continue
            pointer=pointer.next
            
        return dummy.next
        