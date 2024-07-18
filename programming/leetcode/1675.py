class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        
        position.sort()
        n = len(position)
        
        def is_possible(force):
            def func(i):
                return (position[i] - position[l]) > force
            l = 0
            count = 0
            while l < len(position):
                l = bisect.bisect_right(range(n),  key=func, lo=l, x=0)
                count += 1
            return count < m
        
        return bisect.bisect_left(range(1000000000), key=is_possible, x=1)
                    
                
                