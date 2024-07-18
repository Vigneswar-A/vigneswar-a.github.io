class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums)%p
        
        if target == 0:
            return 0
        
        hashmap = {0:-1}
        total = 0
        res = inf

        for i,n in enumerate(nums):
            total += n
            remainder = (total%p - target)%p   
            if remainder in hashmap:
                res = min(i - hashmap[remainder], res)   
            hashmap[total%p] = i
      
        return res if res < len(nums) else -1
        