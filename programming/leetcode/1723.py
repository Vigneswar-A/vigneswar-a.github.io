class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        memo = {}
        office=[0]*n
        
        def dp(bitmask=0):
            if bitmask in memo:
                return memo[bitmask]
            ans = -inf if any(office) else 0
            for i,(u,v) in enumerate(requests):
                if bitmask&(1 << i) == 0:
                    office[v] += 1
                    office[u] -= 1
                    ans = max(dp(bitmask|(1 << i))+1, ans)
                    office[v] -= 1
                    office[u] += 1
            memo[bitmask] = ans
            return ans
        return dp()
                   