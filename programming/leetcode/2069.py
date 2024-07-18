class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = list(accumulate(nums))
        
        def get_counts(target):
            """
            uses sliding window to find number of subarrays with sum less than target
            """
            n = len(nums)
            left = right = count = 0
            sum = nums[0]
            
            while left < n and right < n:
                if sum < target:
                    right += 1
                    if right > left:
                        count += right-left
                    
                    if right < n:
                        sum += nums[right]
                    
                else:
                    sum -= nums[left]
                    left += 1
                    
            return count
                
        left,right = 0,10**9
        while left <= right:
            mid = left+right >> 1
            count = get_counts(mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return right
                
                
            