class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        min_queue = deque()
        max_queue = deque()
        
        ans = 0
        
        left = 0
        for right in range(n):
            while min_queue and nums[min_queue[-1]] >= nums[right]:
                min_queue.pop()
                
            while max_queue and nums[max_queue[-1]] <= nums[right]:
                max_queue.pop()
                
            max_queue.append(right)
            min_queue.append(right)
            
            while min_queue and min_queue[0] < left:
                min_queue.popleft()
                
            while max_queue and max_queue[0] < left:
                max_queue.popleft()
            
            while left < right and nums[max_queue[0]] - nums[min_queue[0]] > limit:
                left += 1
                
                while min_queue and min_queue[0] < left:
                    min_queue.popleft()       
                    
                while max_queue and max_queue[0] < left:
                    max_queue.popleft()
                
                
            ans = max(ans, right-left+1)

            
        return ans
    