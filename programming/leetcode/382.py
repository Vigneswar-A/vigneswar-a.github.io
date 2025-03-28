# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        curr = head
        while curr:
            self.nums.append(curr.val)
            curr = curr.next
    
    def getRandom(self) -> int:
        return choice(self.nums)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()