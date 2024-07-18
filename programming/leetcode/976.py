class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        xmap = defaultdict(set)

        
        for i,j in points:
            xmap[i].add(j)

        res = inf
        x = list(xmap)
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                x0 = x[i]
                x1 = x[j]
                
                for y0 in xmap[x0]:
                    if y0 in xmap[x1]:
                        for y1 in xmap[x0]:
                            if y0 == y1 or y1 not in xmap[x1]:
                                continue
                            res = min(res, abs(x0-x1)*abs(y0-y1))
        return res if res != inf else 0
            
            
        
        