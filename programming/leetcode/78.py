class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for i in nums:
            res += [prev+[i] for prev in res]
            
        return res
            
        