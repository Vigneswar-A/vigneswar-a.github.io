# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        
        currnode = head
        
        
        while currnode:
            for _ in range(m-1):
                if not currnode:
                    break
                currnode = currnode.next
            curr_tail = currnode
            
            for _ in range(n+1):
                if not currnode:
                    break
                currnode = currnode.next
            
            if not curr_tail:
                break
            curr_tail.next = currnode
        
        return head
            
            
            
        