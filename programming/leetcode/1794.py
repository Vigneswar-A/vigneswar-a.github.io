class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        heap = []
        max_ = 0
        
        for num in nums:
            max_value = (2*num if num%2 else num)
            while num%2 == 0:
                num //= 2
            max_ = max(max_, num)
            heapq.heappush(heap, (num, max_value))
            
            
        ans = inf
        
        while heap:
            num, max_value = heapq.heappop(heap)
            ans = min(ans, max_-num)
            
            if num == max_value:
                return ans
            
            heapq.heappush(heap, (2*num, max_value))
            if 2*num > max_:
                max_ = 2*num
        
        return ans
                