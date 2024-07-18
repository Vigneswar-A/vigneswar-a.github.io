class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        know = defaultdict(lambda : '?')
        
        for u, v in knowledge:
            know[u] = v
            
       
        res = temp = ''
        flag = False
        for c in s:
            if c == '(':
                flag = True
            elif c == ')':
                
                res += know[temp]
                flag = False
                temp = ''
                
            elif flag:
                temp += c
                
            else:
                res += c
                
        return res
       
            
        
        
            
            

        