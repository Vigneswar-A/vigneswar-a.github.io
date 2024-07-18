class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.non_zeros[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for idx in self.non_zeros:
            if idx in vec.non_zeros:
                res += self.non_zeros[idx] * vec.non_zeros[idx]
        return res
                
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)