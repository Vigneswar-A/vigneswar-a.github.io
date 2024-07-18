class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        edges = set(map(tuple, edges))
        n += 1
        
        degree = [0]*n
        
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
            
        odds = []
        for i in range(n):
            if degree[i]%2:
                odds.append(i)
                
        
        
        if len(odds) > 4:
            return False
        
        if len(odds) == 4:
            for a, b in combinations(odds, 2):
                temp = [i for i in odds if i != a and i != b]
                c, d = temp
                if (a, b) not in edges and (b, a) not in edges and (c, d) not in edges and (d, c) not in edges:
                    return True
                
        if len(odds) == 2:
            a, b = odds
            if (a, b) not in edges and (b, a) not in edges:
                return True

        if len(odds) == 2:
            a, b = odds
            for i in range(1, n):
                if i != a and i != b and (i, a) not in edges and (a, i) not in edges and (i, b) not in edges and (b, i) not in edges:
                    return True
                
        
        
            
        
        return not odds