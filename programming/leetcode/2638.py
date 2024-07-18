class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        subs = 0
        while i < n:
            left = i
            while i < n and nums[i]%2:
                i += 1
            x = (i-left)
            subs += x*(x+1) // 2
            i += 1
            
        return n*(n+1)//2 - subs
                
            
        