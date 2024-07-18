class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        n = len(garbage)
        res = 0
        travel = [0]+travel
        for c in 'GPM':
            total_dist = 0
            dist = 0
            for s,cost in zip(garbage, travel):
                dist += cost
                if c in s:
                    total_dist += dist + s.count(c)
                    dist = 0
            res += total_dist
        return res
                
            