class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [0] + [*accumulate(arr)]
        n = len(prefix)
        return sum(prefix[j] - prefix[i] for i in range(n - 1) for j in range(i+1 , n , 2))
        