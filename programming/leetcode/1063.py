class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_so_far = 0
        res = 0
        for i in values:
            res = max(res, max_so_far+i-1)
            max_so_far = max(max_so_far-1, i)
           
            
        return res
            