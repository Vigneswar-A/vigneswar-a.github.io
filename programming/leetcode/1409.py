class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        queue = deque([mat])
        cost = 0
        

        def hash(node):
            return ''.join(str(node[i][j]) for i in range(m) for j in range(n))
        
        visited = set()
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if hash(node) in visited:
                    continue
                visited.add(hash(node))
                if all(node[i][j] == 0 for i in range(m) for j in range(n)):
                    return cost
                        
                for i in range(m):
                    for j in range(n):
                        temp = [row[:] for row in node]
                        temp[i][j] = int(not temp[i][j])
                        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                            if 0 <= i+dx < m and 0 <= j+dy < n:
                                temp[i+dx][j+dy] = int(not temp[i+dx][j+dy])
                        queue.append(temp)
            cost += 1
            
        return -1
                
                
                        
            
            