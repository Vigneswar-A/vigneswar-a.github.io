class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return bool(sum(i if i < 10 else -i for i in nums))
        