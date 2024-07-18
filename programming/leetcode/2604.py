class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        
        incs = 0
        res = 0
        for i in range(len(nums1)):
            if nums1[i]%k != nums2[i]%k:
                return -1
            if nums2[i] > nums1[i]:
                incs += (nums2[i]-nums1[i])//k
                res += (nums2[i]-nums1[i])//k
            elif nums2[i] < nums1[i]:
                incs -= (nums1[i]-nums2[i])//k
                
        return res if incs == 0 else -1
                
                
                
            
            
        