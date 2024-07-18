class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        starts = []
        ends = []
        
        for u,v in flowers:
            starts.append(u)
            ends.append(v+1)
            
        starts.sort()
        ends.sort()


        res = []
        for t in people:
            started = bisect.bisect(starts, t)
            ended = bisect.bisect(ends, t)
            res.append(started-ended)
            
        return res