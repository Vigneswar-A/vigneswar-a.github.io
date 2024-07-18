class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        adjacent = defaultdict(list)
        for u,v in adjacentPairs:
            adjacent[u].append(v)
            adjacent[v].append(u)
        
        current = min(adjacent, key=lambda i: len(adjacent[i]))
        visited = {current}
        res = [current]
        while True:
            for adj in adjacent[current]:
                if adj not in visited:
                    res.append(adj)
                    visited.add(adj)
                    current = adj
                    break
            else:
                break
            
        return res
        
            
        
        