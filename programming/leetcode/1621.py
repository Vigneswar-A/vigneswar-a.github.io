class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = 0
        
        while left <= right:
            if nums[left] + nums[right] > target:
                lo = left+1
                hi = right-1
                while lo <= hi:
                    mid = lo + hi >> 1
                    if nums[left]+nums[mid] > target:
                        hi = mid-1
                    else:
                        lo = mid+1
                right = hi
            else:
                left += 1
                ans = (ans + 2**(right-left+1))%(10**9 + 7)
        return ans
        