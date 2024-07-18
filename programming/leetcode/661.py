class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m = len(img)
        n = len(img[0])
        
        def get_avg(x,y):
            total = 0
            count = 0
            for i in range(x-1 , x+2):
                for j in range(y-1 , y+2):   
                    if 0 <= i < m and 0 <= j < n:
                        total += img[i][j]
                        count += 1
            return total // count
                        
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = get_avg(i,j)
                
        return res
                
        