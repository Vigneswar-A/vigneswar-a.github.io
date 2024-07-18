class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        adjacency = [[] for _ in range(n)]

        for u,v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        count = [1]*n
        res = [0]*n
        
        def dfs(node, prev):
            for adj in adjacency[node]:
                if prev == adj:
                    continue
                
                dfs(adj, node)
                count[node] += count[adj]
                res[node] = res[node] + res[adj] + count[adj]
              
        dfs(0, -1)
        stack = [(0, -1)]
        
        while stack:
            node, prev = stack.pop()
            for adj in adjacency[node]:
                if adj == prev:
                    continue
                res[adj] = res[node] - 2*count[adj] + n
                stack.append((adj, node))
        return res
                
        
        