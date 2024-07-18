class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        robots = sorted([[i,a,b,c] for i,(a,b,c) in enumerate(zip(positions, directions,healths))], key=lambda arr:arr[1])
        res = []
        stack = []
        print(robots)
        for i,p,d,h in robots:
            if d == 'R':
                stack.append([i,h])
            else:
                while stack and stack[-1][-1] <= h:
                    if stack[-1][-1] == h:
                        stack.pop()
                        h = 0
                        break
                    else:
                        stack.pop()
                        h -= 1
                    if h == 0:
                        break
                if h and not stack:
                    res.append([i,h])
                elif h and  stack[-1][-1] >= h:
                    stack[-1][-1] -= 1
        res.extend(reversed(stack))
        res.sort()
        return [j for i,j in res]
         
        
        
                
                    
                                  
                
        