class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(i, x):
            if i == len(nums1):
                return 0
            
            res = 0
            if nums1[i] >= x:
                res = max(res, dp(i+1, nums1[i])+1)
            if nums2[i] >= x:
                res = max(res, dp(i+1,nums2[i])+1)
                
            return res
        
        return max(dp(i, 0) for i in range(len(nums1)))