class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        #top-down
        """
        @cache
        def dp(l1=0,l2=0):
            if l1 == len(nums1) or l2 == len(nums2):
                return 0
            if nums1[l1] == nums2[l2]:
                return 1+dp(l1+1,l2+1)
            return max(dp(l1+1,l2),dp(l1,l2+1))
        
        return dp()
        """
    
        #bottom-up
        m,n = len(nums1),len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i] == nums2[j]:           
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]