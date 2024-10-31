class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                
                res += gcd(int(str(nums[i])[0]), nums[j]%10) == 1
                
        return res
        