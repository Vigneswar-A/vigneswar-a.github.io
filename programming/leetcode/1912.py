class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adjacency = defaultdict(list)
        
        for u,v,cost in edges:
            adjacency[u-1].append((v-1, cost))
            adjacency[v-1].append((u-1, cost))     
            
        dist = [inf] * n
        dist[n-1] = 0
        heap = [(0, n-1)]
        visited = set()
        
        while heap:
            cost, node = heappop(heap)
            visited.add(node)
                   
            for v,c in adjacency[node]:
                dist[node] = min(dist[node], cost) 
                if v not in visited and cost+c < dist[v]:
                    dist[v] = cost+c
                    heappush(heap, (dist[v], v))

        @lru_cache(None)
        def dp(node):
            if node == n-1:
                return 1
            ans = 0
            for adj,_ in adjacency[node]:
                if dist[adj] < dist[node]:
                    ans += dp(adj)
            return ans%(10**9+7)

        return dp(0)
                    