class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(first=1,temp=tuple()):
            if len(temp) == k:
                res.append(temp[:])
                return None
            for i in range(first,n+1):
                backtrack(i+1,temp + (i,))
                
        backtrack()
        
        return res