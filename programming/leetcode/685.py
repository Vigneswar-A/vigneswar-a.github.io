class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges) + 1
        adjacency = [[] for _ in range(n)]

        for u,v in edges:
            adjacency[u].append(v)

        def dfs(start):
            stack = [start]
            visited = [0]*n

            while stack:
                node = stack.pop()
                if visited[node]:
                    continue
                visited[node] = 1
                stack.extend(adjacency[node])
            return sum(visited)
        
        roots = []
        for i in range(n):
            if dfs(i) == n-1:
                roots.append(i)

        low = inf
        res = None
        for root in roots:
            for i,(u,v) in enumerate(edges[::-1]):
                adjacency[u].remove(v)
                if dfs(root) == n-1 and i < low:
                    res = (u,v)
                    low = i
                adjacency[u].append(v)
        return res

