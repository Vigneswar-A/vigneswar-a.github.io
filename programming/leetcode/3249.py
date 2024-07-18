class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (reduce(operator.xor, nums) ^ k).bit_count()
        