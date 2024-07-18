
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        return sum(math.comb(i,2) for i in collections.Counter(n-int(str(n)[::-1]) for n in nums).values() if i>1)%1000000007
            
        