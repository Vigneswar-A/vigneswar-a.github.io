class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        remaining = mean*(len(rolls)+n)-sum(rolls)
        
        res = []
        for i in range(n):
            res.append(remaining//(n-i))
            remaining -= res[-1]
            
        if all(1 <= i <= 6 for i in res):
            return res
        
        return []
            
            
            

       

        



        