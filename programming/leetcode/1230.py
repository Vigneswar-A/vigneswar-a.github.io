class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
        res = 0
        for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            prefix =  di*arr1[0]+dj*arr2[0]
            for i in range(len(arr1)):
                res = max(res, (arr1[i]*di+arr2[i]*dj)+i-prefix)
                prefix = min(prefix, arr1[i]*di+arr2[i]*dj+i)
                
        return res
            