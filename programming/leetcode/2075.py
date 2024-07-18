class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
                        
        sweepline = Counter()

        for u,v in lights:
            sweepline[u-v] += 1
            sweepline[u+v+1] -= 1
            
        ans = -inf
        prev = 0
        i = -1
        for (u,v) in sorted(sweepline.items()):
            prev += v
            if prev > ans:
                ans = prev
                i = u
        return i
        
        
        

        