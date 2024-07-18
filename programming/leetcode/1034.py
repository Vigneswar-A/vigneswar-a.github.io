class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counts = Counter()
        res = 0
        left = 0
        for right in range(len(nums)):
            counts[nums[right]] += 1
            while len(counts) > k:
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1
            res += right-left+1
            
        counts = Counter()
        left = 0
        for right in range(len(nums)):
            counts[nums[right]] += 1
            while len(counts) > k-1:
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1
            res -= right-left+1

        return res

        
                
            
        