class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        total = sum(abs(nums1[i]-nums2[i]) for i in range(len(nums1)))
        res = inf
        set_of_nums1 = sorted(set(nums1))
        size = len(set_of_nums1)
        for i in range(len(nums1)):
            j = bisect.bisect(set_of_nums1, nums2[i])
            dec = min((abs(set_of_nums1[idx]-nums2[i]) if idx < size else inf) for idx in (j-1, j, j+1))
            res = min(res, total-(abs(nums1[i]-nums2[i])-dec))
            
        return res%(10**9+7)
            
        