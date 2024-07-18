class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return sum(math.perm(i//2,2)*4 for i in Counter(i*j for i in nums for j in nums if i!=j).values() if i>=4)
                
        