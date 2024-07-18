class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        for row in nums:
            row.sort()
            
        score = 0
        while True:
            max_val = -inf
            for row in nums:
                if row:
                    max_val = max(max_val, row.pop())
            if max_val == -inf:
                break
            score += max_val
            
        return score
            
                
        