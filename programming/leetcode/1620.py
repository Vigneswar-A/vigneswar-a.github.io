class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [i%k for i in arr]
        counts = Counter()
        
        for i in arr:
            if counts[k-i]:
                counts[k-i] -= 1
            else:
                counts[i] += 1
        
        return sum(counts.values())-counts[0] == 0
        