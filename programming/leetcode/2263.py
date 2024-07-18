class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=1)
        extra = sum(batteries[n:])

        def ispossible(m):
            rem = extra
            for i in batteries[:n]:
                rem -= max(m-i, 0)
                if rem < 0:
                    return True
            return False
                

        return bisect.bisect(range(1000000000000000), 0, key=ispossible)-1
        
        
                
            