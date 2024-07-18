class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        res = []
        
            
        for i in range(len(nums)):
            while queue and queue[0] <= i-k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res[k-1:]
            
            
            
            
            
        