class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        import sortedcontainers
        diffs = sortedcontainers.SortedList()
        res = 0
        for a,b in zip(reversed(nums1), reversed(nums2)):
            res += diffs.bisect_left(a-b)
            diffs.add(b-a)
            
        return res
            
        
            
        