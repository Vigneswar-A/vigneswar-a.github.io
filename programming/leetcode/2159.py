class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return (nums1:=set(nums1))&(nums2:=set(nums2))|nums2 & (nums3:=set(nums3))|nums3 & nums1