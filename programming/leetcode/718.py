class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n,m = len(nums1)+1,len(nums2)+1
        
        dp = [[0] * m for _ in range(n)]
        res = 0
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                    res = max(res , dp[i][j])
        return res