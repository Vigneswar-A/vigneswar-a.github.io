class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        min_val = inf
        max_val = -inf

        for i in nums:
            if i < min_val:
                min_val = i
            if i > max_val:
                max_val = i
                
        return gcd(max_val, min_val)