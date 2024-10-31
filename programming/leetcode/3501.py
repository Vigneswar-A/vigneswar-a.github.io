# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        head = ListNode(0, head)
        temp = head
        
        while temp:
            if temp.next and temp.next.val in nums:
                temp.next = temp.next.next
               
            else:
                temp = temp.next
                
        return head.next
                
                
         
        