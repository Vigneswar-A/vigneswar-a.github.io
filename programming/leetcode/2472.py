class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        
        # assign rows
        adjacency = [[] for _ in range(k)]
        degree = [0]*k
        rows = Counter()
        r = 0
        
        for u,v in rowConditions:
            degree[v-1] += 1
            adjacency[u-1].append(v-1)
            
        queue = deque([i for i in range(k) if degree[i] == 0])
        while queue:
            node = queue.popleft()
            rows[node] = r
            r += 1
            for adj in adjacency[node]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)
        if any(degree):
            return []
                    
        # assign cols
        adjacency = [[] for _ in range(k)]
        degree = [0]*k
        cols = Counter()
        c = 0
        
        for u,v in colConditions:
            degree[v-1] += 1
            adjacency[u-1].append(v-1)
            
        queue = deque([i for i in range(k) if degree[i] == 0])
        while queue:
            node = queue.popleft()
            cols[node] = c
            c += 1
            for adj in adjacency[node]:
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)
        
        if any(degree):
            return []
        
        # make matrix
        mat = [[0]*k for _ in range(k)]
        
        for i in range(k):
            mat[rows[i]][cols[i]] = i+1
            
        return mat
        
        