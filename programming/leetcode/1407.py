class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        id = -1
        gcounts = Counter()
       
        
        
        gids = defaultdict(list)
        
        for i,g in sorted(enumerate(groupSizes), key=lambda t:t[1]):
            
            if gcounts[g]%g == 0:
                id += 1
            gcounts[g] += 1
                
            gids[id].append(i)
                
        return gids.values()
                
                
                
         
                
        