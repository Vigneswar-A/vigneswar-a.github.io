class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        res = Counter()
        
        for i,v in nums1+nums2:
            res[i] += v
            
        return sorted(res.items())