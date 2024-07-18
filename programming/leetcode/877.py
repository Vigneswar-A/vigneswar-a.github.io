class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        end = 0
        for i in range(len(graph)):
            end  = end|(1<<i)
            
        @cache
        def dp(node, bitmask, count):
            if bitmask == end:
                return count
            if count == 20:
                return inf
            res = inf
            for adj in graph[node]:
                res = min(res, dp(adj, bitmask|(1<<adj), count+1))
            return res
        
        res = inf
        for i in range(len(graph)):
            res = min(res, dp(i, 1<<i, 0))
                      
        return res
            
                        
                    
                    
                
                
            
        