class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapq.heapify(heap)
        res = 0
        
        for _ in range(k):
            max = -heapq.heappop(heap)
            res += max
            heapq.heappush(heap, -ceil(max/3))
        
        return res
        