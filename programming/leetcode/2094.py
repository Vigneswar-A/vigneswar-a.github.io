class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapify(heap)
        for _ in range(k):
            pile = -heappop(heap)
            heappush(heap, -pile+pile//2)
        
        return -sum(heap)
        
        