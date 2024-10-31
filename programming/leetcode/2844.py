class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        return sum(j*j for i, j in enumerate(nums,1) if len(nums)%i == 0)
        
        
        