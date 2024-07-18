class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        counts = Counter(changed)
        heap = [-i for i in changed]
        heapq.heapify(heap)

        if len(changed)%2:
            return []
        
        res = []
        
        while heap:
            highest = -heapq.heappop(heap)
            if counts[highest] == 0:
                continue
                
            if counts[highest/2] > 0:
                counts[highest/2] -= 1
                counts[highest] -= 1
                res.append(highest//2)
            else:
                return []
               
        return res
            
        