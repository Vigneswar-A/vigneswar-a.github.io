from collections import Counter
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(comb(i,2) for i in Counter(nums).values())
        
            