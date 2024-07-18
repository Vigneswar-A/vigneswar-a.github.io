class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)-1,-1,-1):
            while len(heap) > 0 and heap[0][1]-i > k:
                heappop(heap)
            if not heap:
                heappush(heap, (-nums[i], i))
            else:
                heappush(heap,  (heap[0][0]-nums[i], i))
               
        for score, idx in heap:
            if idx == 0:
                return -score
            
            
                    
        
            