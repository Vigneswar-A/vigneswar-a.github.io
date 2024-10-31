class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        less = []
        more = []
        
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    less.append((i,j))
                elif grid[i][j] > 1:
                    more.append([i,j, grid[i][j]])
        queue = deque([(less, more, 0)])
        ans = inf
        while queue:
            
            for _ in range(len(queue)):
                
                less, more, moves = queue.popleft()
                if not less:
                    
                    ans = min(ans, moves)
                    print(ans)
                    continue
                for i in range(len(less)):
                    for j in range(len(more)):
                        more[j][-1] -= 1
                     
                        queue.append(([row[:] for x,row in enumerate(less) if i != x], [row[:] for row in more if row[-1] > 1], moves+abs(less[i][0]-more[j][0])+abs(less[i][1]-more[j][1])))
                        more[j][-1] += 1
                        
        return ans
                       
                    
                  
                    
        
            
        