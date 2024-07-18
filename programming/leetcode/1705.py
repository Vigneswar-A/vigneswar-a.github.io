class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        
        rank = [[0]*n for _ in range(n)]
        
        for i in range(n):
            pref = n-1
            for j in range(n-1):
                rank[i][preferences[i][j]] = pref
                pref -= 1
        

        unhappy = [0]*n
        for i in range(len(pairs)):
            for j in range(i+1, len(pairs)):
                x,y = pairs[i]
                u,v = pairs[j]
                
                if rank[x][u] > rank[x][y] and rank[u][x] > rank[u][v]:
                    unhappy[x] = 1
                    unhappy[u] = 1
                    
                if rank[y][u] > rank[y][x] and rank[u][y] > rank[u][v]:
                    unhappy[y] = 1
                    unhappy[u] = 1
                    
                if rank[x][v] > rank[x][y] and rank[v][x] > rank[v][u]:
                    unhappy[x] = 1
                    unhappy[v] = 1
                    
                if rank[y][v] > rank[y][x] and rank[v][y] > rank[v][u]:
                    unhappy[y] = 1
                    unhappy[v] = 1
                    
                
                    
                
                    
        return sum(unhappy)
                
        
        