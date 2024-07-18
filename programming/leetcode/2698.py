class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        queue = deque([*map(str, nums)])
        res = 0
        while len(queue) > 1:
            res += int(queue.popleft()+queue.pop())
        return res+(int(queue.pop()) if queue else 0)
        
    
            
         
            
            
        