class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def cross_sum(left, right):
            left_sum = 0
            mid = left+right >> 1
            sum = 0
            for i in range(mid-1, left-1, -1):
                sum += nums[i]
                left_sum = max(left_sum, sum)
                
            sum = 0
            right_sum = 0
            for i in range(mid+1, right+1):
                sum += nums[i]
                right_sum = max(right_sum, sum)

            return nums[mid] + left_sum + right_sum
                
            
        
        def dac(left=0, right=len(nums)-1):
            if left > right:
                return -inf
            mid = left+right >> 1
            return max(dac(left, mid-1), dac(mid+1, right), cross_sum(left, right))
        
        return dac()
            