class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_idx = max_idx = 0
        
        for i in range(n := len(nums)):
            if nums[i] < nums[min_idx]:
                min_idx = i
            elif nums[i] >= nums[max_idx]:
                max_idx = i

        return (n-max_idx-1)+min_idx-(min_idx > max_idx)
        