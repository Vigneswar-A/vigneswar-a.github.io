class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1:
            return 1
        adjacency = defaultdict(list)
        for u,v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
            
        visited = set()
        res = 0
        def dfs(node=0):
            nonlocal res
            total = values[node]
            for child in adjacency[node]:
                if child in visited: continue
                visited.add(child)
                child_sum = dfs(child)
                if child_sum%k == 0:
                    res += 1
                    child_sum = 0
                total += child_sum
            return total
                
        dfs()
        return res
                
                
            
                    

        