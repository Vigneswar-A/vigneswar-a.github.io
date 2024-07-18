# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = None
        currnode = head
        
        while currnode:
            temp = currnode
            currnode = currnode.next
            temp.next = newhead
            newhead = temp
            
            
        return newhead
            