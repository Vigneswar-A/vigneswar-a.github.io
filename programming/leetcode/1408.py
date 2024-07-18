class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        
        isvalid = lambda div : sum(math.ceil(n / div) for n in nums) <= threshold
        
        while left < right:
            
            mid = (left + right) // 2
            
            if isvalid(mid):
                right = mid
            else:
                left = mid + 1
           

        return right
                
            
        