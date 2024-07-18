# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            if not (head and head.next):
                return head
            if head.val == head.next.val:
                currnode = head
                while currnode and currnode.val == head.val:
                    currnode = currnode.next
                return helper(currnode)
            else:
                head.next = helper(head.next)
                return head
        return helper(head)
                
        
                
                    
                    
            