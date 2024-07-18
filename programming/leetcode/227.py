class Solution:
    def calculate(self, s: str) -> int:
        
        def parse(s):
            temp = ''
            for c in s:
                if c.isdigit():
                    temp += c
                elif c != ' ':
                    yield temp
                    temp = ''
                    yield c
            yield temp
                    
        def solve(terms):
            for i in range(len(terms)):
                if terms[i] == '*':
                    terms[i-1:i+2] = [None,None,int(terms[i-1])*int(terms[i+1])]
                elif terms[i] == '/':
                    terms[i-1:i+2] = [None,None,int(terms[i-1])/int(terms[i+1])]
                    
            res = 0
            pos = True
            for c in filter(None, terms):
                if c == '+':
                    pos = True
                elif c == '-':
                    pos = False
                else:
                    res += (int(c) if pos else -int(c))
            return res
                
        List = [*parse(s)]
        return solve(List)
                