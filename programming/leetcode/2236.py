# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        max_twin_sum = -float('inf')
        for i in range(len(nums) // 2):
            max_twin_sum = max(max_twin_sum , nums[i] + nums[-i - 1])
            
        return max_twin_sum
            
            