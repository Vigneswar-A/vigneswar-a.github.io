class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = list(accumulate(arr, int.__xor__))+[0]
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if prefix[i-1]^prefix[j] == 0:
                    res += (j-i)
        return res
                    