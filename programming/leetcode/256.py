class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @cache
        def dp(prev=None, idx=0):
            if idx == len(costs):
                return 0
            
            res = float('inf')
            for i in range(3):
                if i == prev:
                    continue
                res = min(res , dp(i , idx+1)+costs[idx][i])
                
            return res        
        
        return dp()
                
        
        