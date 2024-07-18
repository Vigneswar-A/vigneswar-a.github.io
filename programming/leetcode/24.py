# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head.next
            head.next = head.next.next
            temp.next = head
            temp.next.next = self.swapPairs(temp.next.next)
            return temp
        return head