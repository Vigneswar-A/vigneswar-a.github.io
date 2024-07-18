class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        result = []
        def backtrack(s):
            if len(s) == n:
                result.append(s)
                
            elif len(s) > n or s[0] == '0':
                return None
                
            last_digit = int(s[-1])
            for i in range(10):
                if abs(last_digit - i) == k:
                    backtrack(s+str(i))
              
        for i in range(10):
            backtrack(str(i))
            
        return map(int , result)
                
        