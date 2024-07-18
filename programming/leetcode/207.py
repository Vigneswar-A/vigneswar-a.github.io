class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        
        in_degree = {}
        adj = defaultdict(list)
        for i in range(n):
            in_degree[i] = 0
            
            
        for u,v in pre:
            adj[v].append(u)
            in_degree[u] += 1
            
        stack = [i for i,j in in_degree.items() if j == 0]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(node)
            for next in adj[node]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    stack.append(next)
        return len(visited) == n
        
        