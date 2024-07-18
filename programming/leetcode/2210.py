class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        g=l=t=0
        for i in nums:
            if i<target:
                l+=1
            elif i>target:
                g+=1
            t+=1
        return range(l,t-g)
        