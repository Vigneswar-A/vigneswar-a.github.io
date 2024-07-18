class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        return bisect.bisect(range(1000000000), 0, key=lambda moves : sum(max((i-moves*y-1)//(x-y) + 1, 0) for i in nums) <= moves)