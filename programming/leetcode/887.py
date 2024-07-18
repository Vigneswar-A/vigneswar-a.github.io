class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        ratios = sorted((w/q,q) for i,(w,q) in enumerate(zip(wage, quality)))
        heap = []
        quals = 0
        res = inf
        count = 0
        
        for r,q in ratios:
            heappush(heap, -q)
            quals += q
            
            if len(heap) > k:
                quals += heappop(heap)
            
            if len(heap) == k:
                res = min(res, quals*r)
                
        return res
                
        