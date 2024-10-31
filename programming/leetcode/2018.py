class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        
        packages.sort()
        prefix = list(accumulate(packages))+[0]
        res = inf
        
        for box in boxes:
            box.sort()
            l = 0
            waste = 0
            for size in box:
                r = bisect.bisect(packages, size)
                
                waste += size*(r-l)-(prefix[r-1]-prefix[l-1])
                l = r
                
                if r >= len(packages):
                    res = min(res, waste)
                    break
            
        return res%1000000007 if res != inf else -1
            
                
        
        
        
        