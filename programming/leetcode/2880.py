class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        
        adjacency = defaultdict(list)
        for u,v,c in edges:
            adjacency[u].append((v, c))
            
        heap = [(0, s)]
        visited = set()
        
        while heap:
            min_dist, min_node = heappop(heap)
            visited.add(min_node)
            if min_node in marked:
                return min_dist
            for adj,dist  in adjacency[min_node]:
                if adj not in visited:
                    heappush(heap, (min_dist+dist, adj))
        
        return -1
                    
        