class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        least = inf
        most = -inf
        res = -inf
        
        for i in range(len(arrays)):
            res = max(res, most-arrays[i][0], arrays[i][-1]-least)
            most = max(most, arrays[i][-1])
            least = min(least, arrays[i][0])
            
        return res
    
        