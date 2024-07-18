class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        m,n = len(mat),len(mat[0])
        prefix = [[0]*(n+1) for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                prefix[i][j] = prefix[i][j-1] + mat[i][j]
               
            
        def square_sum(x, y, side):
            temp = 0
            for k in range(side+1):
                temp += prefix[i+k][j+side] - prefix[i+k][j-1]
            return temp
            
        res = 0
        for i in range(m):
            for j in range(n):
                left = 0
                right = min(m-i, n-j)-1
                while left <= right:
                    mid = left+right >> 1
                    if square_sum(i, j, mid) > threshold:
                        right = mid-1
                    else:
                        left = mid+1
                        res = max(res, mid)
                res = max(res, left)
        
        return res

   # [[1,1,1,1],
   #  [1,1,1,1],
   #  [1,1,1,1]]