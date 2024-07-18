class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def get_neighbours(board):
            zx = 0 if 0 in board[0] else 1
            zy = board[zx].index(0)

            for dx,dy in [(1,0), (-1,0), (0,-1), (0,1)]:
                if 0 <= dx+zx <= 1 and 0 <= dy+zy <= 2:      
                    board[zx+dx][dy+zy], board[zx][zy] = board[zx][zy], board[zx+dx][zy+dy] 
                    yield copy.deepcopy(board)
                    board[zx+dx][dy+zy], board[zx][zy] = board[zx][zy], board[zx+dx][zy+dy]

        def get_hash(board):
            return tuple(board[0]),tuple(board[1])

        
        visited = set()
        depth = 0
        queue = deque([board])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                hash = get_hash(node)
                if node == [[1,2,3],[4,5,0]]:
                    return depth
                if hash in visited:
                    continue
                visited.add(hash)
                queue.extend(get_neighbours(node))
            depth += 1
        return -1

                    
        