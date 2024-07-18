# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        res = 0
        curr = head
        
        while curr:
            res = res * 10 + curr.val
            curr = curr.next
        
        new = ListNode()
        curr = new
        
        for i in map(int , str(res + 1)): 
            curr.next = ListNode(i)
            curr = curr.next
            
        return new.next
            
            
        