class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        queue = deque(s)
        
        for u,v in shift:
            if not u:
                for _ in range(v):
                    queue.append(queue.popleft())
            else:
                for _ in range(v):
                    queue.appendleft(queue.pop())
                    
        return ''.join(queue)
        