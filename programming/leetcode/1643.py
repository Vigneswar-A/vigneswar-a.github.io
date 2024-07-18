class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        adjacency = [[] for _ in range(n)]
        visited = set([0])

        for u,v in edges:
            if u in visited:
                adjacency[u].append(v)
                visited.add(v)
            elif v in visited:
                adjacency[v].append(u)
                visited.add(u)
        

        counts = [Counter() for _ in range(n)]

        def update(root):
            for child in adjacency[root]:
                update(child)
                counts[root].update(counts[child])
            counts[root][labels[root]] += 1
        
        update(0)
        return [counts[i][labels[i]] for i in range(n)]

                