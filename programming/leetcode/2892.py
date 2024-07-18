class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return Counter(nums) == Counter(range(1, (n:=len(nums)-1)))|Counter([n]*2)
                                        