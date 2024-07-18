class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([x])
        cost = 0
        bound = abs(x-y)
        seen = {x}
        while queue:
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == y:
                    return cost
                
                    
                
                if node+1 not in seen:
                    queue.append(node+1)
                    seen.add(node+1)
                if node-1 not in seen:
                    queue.append(node-1)
                    seen.add(node-1)
                if node%5 == 0:
                    if node//5 not in seen:
                        queue.append(node//5)
                        seen.add(node//5)
                        
                if node%11 == 0:
                    if node//11 not in seen:
                        queue.append(node//11)
                        seen.add(node//11)
            cost += 1
    
    
    
    
        