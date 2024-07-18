class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        directions = [(i , j) for i in (-2 , -1 , 1 , 2) for j in (-2 , -1 , 1 , 2) if abs(i)!=abs(j)]
        seen = set()
        queue = collections.deque([(0 , 0)])
        dest = (x,y)
        dist = 0
        
        while queue:
            for _ in range(len(queue)):
                x , y = queue.popleft()

                if (x,y) in seen:
                    continue

                seen.add((x,y))

                if (x,y) == dest:
                    return dist

                for i , j in directions:
                    queue.append((x + i , y + j))
            dist += 1

        return -1