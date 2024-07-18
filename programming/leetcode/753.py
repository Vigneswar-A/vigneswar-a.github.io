class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([('0000',0)])
        seen = set()
        
        while queue:
            node, count = queue.popleft()
            if node in seen or node in deadends:
                continue
                
            if node == target:
                return count
               
            seen.add(node)
            currnode = list(map(int , node))
            
            for i in range(4):
                if currnode[i] < 9:
                    currnode[i] += 1
                    queue.append((''.join(map(str , currnode)) , count+1))
                    currnode[i] -= 1
                if currnode[i] > 0:
                    currnode[i] -= 1
                    queue.append((''.join(map(str , currnode)) , count+1))
                    currnode[i] += 1
                if currnode[i] == 0:
                    temp , currnode[i] = currnode[i] , 9
                    queue.append((''.join(map(str , currnode)) , count+1))
                    currnode[i] = temp
                if currnode[i] == 9:
                    temp , currnode[i] = currnode[i] , 0
                    queue.append((''.join(map(str , currnode)) , count+1))
                    currnode[i] = temp
                    
        return -1
            
                    
                    
                
        
        