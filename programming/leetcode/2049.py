class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        prev_time = charges = kills = 0
        for i in sorted(ceil(d/s) for d,s in zip(dist,speed)):
            charges += (i-prev_time-1)
            if charges >= 0:
                kills += 1
            else:
                break
            prev_time = i
                
        return kills