class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        res1 = res2 = 0
        for i in set(nums1):
            res1 += counts2[i]
            
        for i in set(nums2):
            res2 += counts1[i]
            
        return [res2, res1]
            
        
            
        
         
        
        