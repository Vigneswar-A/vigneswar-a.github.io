class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
         
        @cache
        def backtrack(n , start = 2):
            res = []
            for i in range(start , int(n**0.5) + 1):
                if n%i == 0:
                    res.append([n//i , i])
                    res.extend(path + [i] for path in backtrack(n//i , i))
            return res
            
        return backtrack(n)