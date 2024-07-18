class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        A,N,_,B,M = s
        res = []
        
        if N == M:
            for i in range(ord(A), ord(B)+1):
                res.append(chr(i) + M)
        else:
            for i in range(ord(A), ord(B)+1):
                for j in range(int(N), int(M)+1):
                    res.append(chr(i)+str(j))
          
        return res
            