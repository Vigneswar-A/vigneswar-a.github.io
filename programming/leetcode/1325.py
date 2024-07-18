class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        heap = [(-1, start)]
        heapq.heapify(heap)

        adjacency = [[] for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            adjacency[u].append((succProb[i], v))
            adjacency[v].append((succProb[i], u))

        visited = set()
        while heap:
            prob, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return -prob
            for cost,adj in adjacency[node]:
                heapq.heappush(heap, (cost*prob, adj))

        return 0
        
            
