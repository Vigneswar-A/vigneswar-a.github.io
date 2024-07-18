class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        available = []
        best = []
        
        for c in counts:
            heappush(available, (0, c))
            
        time = 0
        while available or best:
            while available and nsmallest(1, available)[0][0] <= time:
                t, c = heappop(available)
                heappush(best, (-counts[c], c))
            
            if not best:
                time += 1
                continue
                
            
            _, c = heappop(best)
            time += 1
            counts[c] -= 1
            
            if counts[c]:
                heappush(available, (time+n, c))
                
        return time
            
            
            
            
        
            
                
            
        
        
     
        
        
        
        
        