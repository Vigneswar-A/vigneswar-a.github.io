# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find the center
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        # reverse the second part
        newhead = None
        while mid:
            temp = mid.next
            mid.next = newhead
            newhead = mid
            mid = temp
        
        
        # merge them
        left = head
        right = newhead
        
        while left and right:
            temp1 = left.next
            temp2 = right.next
            left.next = None
            right.next = None
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2
            
            
            