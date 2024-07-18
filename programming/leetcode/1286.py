class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        dp = [0] * n
        ans = -inf
        queue = deque([])
        
        for i in range(n):
            dp[i] = max([*(dp[i] for i in queue), 0]) + nums[i]
            ans = max(ans, dp[i])
            while queue and i-queue[0] >= k:
                queue.popleft()
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
                
            queue.append(i)
              
        return ans
                