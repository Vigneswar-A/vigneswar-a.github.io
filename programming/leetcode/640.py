import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        LHS,RHS=equation.split("=")
        LHS=[i for i in re.split(r'([\d]+x|[\d]+|[+-]?|)',LHS) if i!='']
        RHS=[i for i in re.split(r'([\d]+x|[\d]+|[+-]?)',RHS) if i!='']
        def simplify(s):
            ce=0
            n=0
            for i in range(len(s)):
                if 'x' in s[i]:
                    if i>0 and s[i-1]=='-':
                        ce-=int(s[i].replace('x','')) if len(s[i])>1 else 1
                    else:
                        ce+=int(s[i].replace('x','')) if len(s[i])>1 else 1                  
                elif s[i].isdigit():
                    if i>0 and s[i-1]=='-':
                        n-=int(s[i])
                    else:
                        n+=int(s[i])
            return (ce,n)
        a,b,c,d=*simplify(LHS),*simplify(RHS)
        if a!=c:
            return f'x={int(-(d-b)/(c-a))}'
        elif a==c and b==d:
            return 'Infinite solutions'
        elif a==c and b!=d:
            return 'No solution'           
        
        
        
                
            
    
        
                
                
            
            
        
    
        