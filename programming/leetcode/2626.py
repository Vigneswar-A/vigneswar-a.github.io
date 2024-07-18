class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        pairs = 0
        counts = Counter()
        res = 0
        left = 0
        for right in range(len(nums)):
            pairs += counts[nums[right]]
            counts[nums[right]] += 1
        
            while pairs >= k:
                counts[nums[left]] -= 1
                pairs -= counts[nums[left]]
                left += 1
            res += left
        
            
        return res
                
                
            