class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def isprime(num):
            if num == 1:
                return False
            for i in range(2, int(sqrt(num))+1):
                if num%i == 0:
                    return False
            return True
                
        n = len(nums)
        res = 0
        
        for i in range(n):
            if isprime(nums[i][i]):
                res = max(res, nums[i][i])
            if isprime(nums[i][-i-1]):
                res = max(res, nums[i][-i-1])
                
        return res
                