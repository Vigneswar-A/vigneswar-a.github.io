class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])

        @cache
        def dp(prev=None, idx=0):
            if idx == len(costs):
                return 0
            
            res = float('inf')
            for i in range(k):
                if i == prev:
                    continue
                res = min(res , dp(i , idx+1)+costs[idx][i])
                
            return res        
        
        return dp()
                