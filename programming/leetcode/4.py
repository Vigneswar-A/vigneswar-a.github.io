class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = sorted(nums1 + nums2)
        if (size:=len(median))%2:
            return median[size//2]
        else:
            return (median[size//2] + median[size//2 - 1])/2