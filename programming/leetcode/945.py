class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
          
        def get_coords(i):
            i -= 1
            row = n - i//n - 1
            col = i%n if (n - row - 1)%2==0 else n - i%n - 1
            return row, col
        

        def get_nei(curr):
            for nxt in range(curr+1, min(curr+6, n**2)+1):
                i,j = get_coords(nxt)
                if board[i][j] == -1:
                    yield nxt
                else:
                    yield board[i][j]
                    
        queue = deque([1])
        moves = 0
        visited = [0] * (n**2 + 1)
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if visited[node]:
                    continue
                visited[node] = 1
                if node == n*n:
                    return moves
                queue.extend(get_nei(node))
            moves += 1
           
            
        return -1
