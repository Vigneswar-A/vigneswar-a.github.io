class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            nums = list(map(int, str(i)))
            n = len(nums)
            if n%2: continue
            res += sum(nums[:n//2])==sum(nums[n//2:])
        return res
            
        