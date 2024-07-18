class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        queue = deque()
        flips = 0
        for i in range(len(nums)):
            if queue and queue[0] == i:
                queue.popleft()
            if (nums[i]+len(queue))%2 == 0:
                flips += 1
                queue.append(i + k)
                if i+k > len(nums):
                    return -1
                
        return flips
                
        