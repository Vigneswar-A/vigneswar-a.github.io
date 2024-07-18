class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        squares1 = Counter(i*i for i in nums1)
        squares2 = Counter(i*i for i in nums2)
        count = 0
        
        for i in range(size := len(nums1)):
            for j in range(i):
                if nums1[i] * nums1[j] in squares2:
                    count += squares2[nums1[i] * nums1[j]]
                        
        for i in range(size := len(nums2)):
            for j in range(i):
                if nums2[i] * nums2[j] in squares1:
                    count += squares1[nums2[i] * nums2[j]]
                        
        return count
                
                        
        