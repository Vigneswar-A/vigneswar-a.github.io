from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        currentmax=0
        for i in (c:=Counter(nums)):
            currentmax=max(currentmax,c[i]+c[i+1]) if i+1 in c else currentmax
        return currentmax
            
                    