class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0]+nums2[0], 0, 0)]
        res = []
        visited = set()
        
        while k and heap:
            sum, i, j = heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i, j))
            
            k -= 1
            res.append((nums1[i], nums2[j]))
            
            if i+1 < len(nums1):
                heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                
            if j+1 < len(nums2):
                heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            
        return res
            
        
            
                
        
        
            
            