class Solution:
    def racecar(self, target: int) -> int:
        
        
        queue = deque([(0, 1)])
        steps = 0
        visited = set()
        
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if (pos, speed) in visited:
                    continue
                visited.add((pos, speed))
                if pos == target:
                    return steps
                queue.append((pos + speed, speed*2))
                queue.append((pos, (-1 if speed > 0 else 1)))
            steps += 1
            
        