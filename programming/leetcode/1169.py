class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        items = sorted(zip(values, labels), reverse=1)
        counts = Counter()
        res = 0
        used = 0
        
        for value,label in items:
            if used == numWanted:
                break
            if counts[label] < useLimit:
                res += value
                counts[label] += 1
                used += 1
                
        return res
                
            
                
        