class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        stop = a+b+max(x, max(forbidden))
        
        queue = deque([(0, 1)])
        seen = set()
        depth = 0
        
        while queue:
            for _ in range(len(queue)):
                pos, can_move_back = queue.popleft()
                if (pos, can_move_back) in seen:
                    continue
                seen.add((pos, can_move_back))
                if pos == x:
                    return depth
                
                if pos < 0 or pos in forbidden or pos > stop:
                    continue
                    
                if can_move_back:
                    queue.append((pos-b, 0))
                
                queue.append((pos+a, 1))
                
            depth += 1
                
                
        return -1