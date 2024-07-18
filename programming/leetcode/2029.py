class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1.sort()
        nums2.sort(reverse=1)
        
        return sum(i*j for i,j in zip(nums1, nums2))