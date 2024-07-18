class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        nums = [0]*(n+1)
        for center,radius in enumerate(ranges):
            start = max(0, center-radius)
            end = min(n, center+radius)
            nums[start] = max(nums[start], end)
            
        jumps = 0 
        farthest = 0 
        reachable = 0 
        
        for i in range(n+1):
            if i > farthest:
                return -1
            if i > reachable:
                jumps += 1
                reachable = farthest
            farthest = max(farthest, nums[i])
            
        return jumps           