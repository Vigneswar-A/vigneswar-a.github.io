class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort(reverse = 1)
        count = 0
        
        for i in range(len(g)):
            while s and s[-1] < g[i]:      
                s.pop()
                
            if s:
                count += 1
            else:
                break
               
            s.pop()
                        
        return count 
        