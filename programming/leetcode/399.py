
from collections import deque, defaultdict
from itertools import starmap

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = lambda : defaultdict(graph)
        adj = graph()
        
        for node, cost in zip(equations, values):
            u, v = node
            adj[u][v] = cost
            adj[v][u] = -cost

        def bfs(start, dest):
            if start not in adj:
                return -1
            queue = deque([(start, 1)])
            seen = set()
            while queue:
                node, cost = queue.pop()
                if node in seen: continue
                seen.add(node)
                if node == dest:
                    return cost
                for adjnode in adj[node]:
                    nextcost = adj[node][adjnode] 
                    if nextcost >= 0:
                        queue.append((adjnode, cost*nextcost))
                    else:
                        queue.append((adjnode, cost/(-nextcost)))
            return -1

        return list(starmap(bfs, queries))

            


        