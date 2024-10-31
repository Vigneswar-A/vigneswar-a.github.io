class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort(reverse=1)
        cuboids.sort(reverse=1)
        
        
        n = len(cuboids)
        @cache
        def dp(i):
            
          
   
            res = 0
            for j in range(i+1, n):
                if all(cuboids[j][k] <= cuboids[i][k] for k in range(3)):
                    res = max(res, dp(j)+cuboids[j][0])
            return res
        
        return max(dp(i)+cuboids[i][0] for i in range(n))
                    
                
        