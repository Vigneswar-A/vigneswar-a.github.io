class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        seen = set()
        
        def backtrack(code=['0']*n):
            s = int(''.join(code), 2)
            if s in seen:
                return
            
            seen.add(s)
            res.append(s)
            
            for i in range(n):
                if code[i] == '0':
                    code[i] = '1'
                    backtrack(code)
                    code[i] = '0'
                else:
                    code[i] = '0'
                    backtrack(code)
                    code[i] = '1'
                    
        backtrack()
        return res
                
            
            
        