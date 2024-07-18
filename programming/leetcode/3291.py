class Solution:
    def canSortArray(self, nums: List[int]) -> bool:    
        bits = {i:i.bit_count() for i in nums}
        
        n = len(nums)
        for _ in range(n):
            for i in range(n-1):
                if nums[i+1] < nums[i] and bits[nums[i+1]] == bits[nums[i]]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums == sorted(nums)