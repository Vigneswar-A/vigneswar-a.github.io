class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        def square(num):
            for i in range(2, num):
                count = 0
                while num%i == 0:
                    num //= i
                    count += 1
                if count > 1:
                    return True
            return False
        
        newnums = []
        for i in nums:
            if not square(i):
                newnums.append(i)
        del nums
        nums = newnums
        n = len(nums)
        
        cache = defaultdict(lambda : defaultdict(lambda : -1))
        def dp(i=0, num=1):
            if i == n:
                return 1
            if cache[i][num] == -1:
                if gcd(num, nums[i]) == 1:
                    cache[i][num] = (dp(i+1, num*nums[i])+dp(i+1, num))%(1000000007)
                else:
                    cache[i][num] = dp(i+1, num)%(1000000007)
                    
            return cache[i][num]
        
        return (dp()-1)%(1000000007)