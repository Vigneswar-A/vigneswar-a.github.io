class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        pop = {'B':'A', 'D':'C'}
        
        for i in s:
            

            if i in pop and stack and stack[-1] == pop[i]:
                stack.pop()
            else: 
                stack.append(i)
                
                
        return len(stack)
        