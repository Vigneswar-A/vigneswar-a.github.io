class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        m = len(workers)
        n = len(bikes)
        
        bmask = 0
            
        for i in range(n):
            bmask |= (1 << i)

        @cache
        def get_dist(worker, j):
            bx,by = bikes[j]
            wx,wy = workers[worker]        
            return abs(bx-wx) + abs(by-wy)
        
        @cache
        def dp(worker=0, bm=bmask):
            if worker == m:
                return 0

            res = float('inf')
            for i in range(n):
                if bm&(1<<i):
                    res = min(res, get_dist(worker, i) + dp(worker+1, bm-(1<<i)))  

            return res
        
        return dp()
                        
                    
                    
                
        