class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        farthest = 0
        reachable = 0
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == reachable:
                jumps += 1
                reachable = farthest
            
            
        return jumps
                