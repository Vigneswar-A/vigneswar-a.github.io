class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        heap = [1]
        res = set()
        
        while len(res) < n:
            i = heappop(heap)
            
            
            
           
            for j in [2, 3, 5]:
                if i*j not in res and i*j not in heap:
                    heappush(heap, i*j)
            res.add(i)
            
        return i
                    
        