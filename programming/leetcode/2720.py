class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        
        def possible(target):
            count = 0
            i = 0
            while i < len(nums)-1:
                if nums[i+1]-nums[i] <= target:
                    count += 1
                    i += 1
                i += 1
            return count >= p

        return bisect.bisect_left(range(max(nums)), 1, key=possible)
        
        
        
        