class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [
(-counts.get(i), i) for i in counts]
        
        heapq.heapify(heap)
        
        res = []
        while heap:

            count ,i = heappop(heap)
            if not res or res[-1] != i:
                res.append(i)
  
                if count+1:
                    heappush(heap, (count+1, i))
                continue
                         
            if res[-1] == i:
                 if not heap:
                     return ''
                 count2, i2 = heappop(heap)
                         
                 res.append(i2)
                 if count2+1:
                     heappush(heap, (count2+1, i2))
                 heappush(heap, (count, i))
        return ''.join(res)
                             

                 
                         
                         
                
     
            
        