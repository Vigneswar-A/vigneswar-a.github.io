class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        adjacency = [[] for _ in range(n+1)]
        for u,v,cost in connections:
            adjacency[u].append((cost, v))
            adjacency[v].append((cost, u))

        heap = [(0,1)]
        heapq.heapify(heap)
        visited = [0]*(n+1)
        total = 0
        edges = 0

        while heap and edges < n:
            cost, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = 1
            total += cost
            edges += 1
            for next in adjacency[node]:
                heapq.heappush(heap, next)

        return total if edges == n else -1

                       


        