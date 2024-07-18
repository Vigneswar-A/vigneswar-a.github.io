from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(i for i,j in Counter(nums).items() if j==1)
        