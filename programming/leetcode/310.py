class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency = [set() for _ in range(n)]

        for u,v in edges:
            adjacency[u].add(v)
            adjacency[v].add(u)

        remaining = n
        leaves = [node for node in range(n) if len(adjacency[node]) == 1]

        while remaining > 2:
            remaining -= len(leaves)
            new_leaf = []

            for leaf in leaves:
                adj = adjacency[leaf].pop()
                adjacency[adj].remove(leaf)
                if len(adjacency[adj]) == 1:
                    new_leaf.append(adj)
            
            leaves = new_leaf

        return leaves or [0]