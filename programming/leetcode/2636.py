class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = sorted(zip(nums2, nums1), reverse=1)
        sum = 0
        heap = []

        res = 0
        for j,i in arr:
            if len(heap) < k:
                heapq.heappush(heap, i)
                sum += i
            elif i > heap[0]:
                sum += i - heapq.heappushpop(heap, i)
            if len(heap) == k:
                res = max(res, sum*j)
            
        return res
                
            
                
        
        
        
        
        