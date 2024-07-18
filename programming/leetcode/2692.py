class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-i for i in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            gift = heappop(heap)
            heappush(heap, -isqrt(abs(gift)))
            
        return -sum(heap)
        