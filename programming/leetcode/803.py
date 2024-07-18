class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # bellman ford
        prev = [inf]*n
        prev[src] = 0
        
        for _ in range(k+1):
            curr = prev[:]
            for u,v,c in flights:
                curr[v] = min(prev[u]+c, curr[v])
            prev = curr

        return curr[dst] if curr[dst] != inf else -1