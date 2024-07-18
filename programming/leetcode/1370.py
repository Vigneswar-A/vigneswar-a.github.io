class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [-1] + [i for i, v in enumerate(nums) if v%2==1] + [len(nums)]
        return sum((odds[i] - odds[i-1]) * (odds[i-k] - odds[i-k-1]) for i in range(k+1, len(odds)))