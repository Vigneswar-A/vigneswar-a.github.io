class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        reqsum = sum(nums)-x
        

        left = 0
        res = 0
        length = -1
        
        for right in range(len(nums)):
            res += nums[right]
            while left <= right and res > reqsum:
                
                res -= nums[left]
                left += 1
            
            if reqsum == res:
                length = max(length, right-left+1)
                
        return len(nums)-length if length != -1 else -1
                
            
        
        
        
        
        