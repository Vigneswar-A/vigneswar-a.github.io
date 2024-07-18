class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
        
        nums.sort()
        target.sort()
        
        def solve(nums, target):
            res = 0
            extra = 0
            for i in range(len(nums)):
                res += max((nums[i]-target[i])//2, 0)

            return res
        
        odds = []
        odds_target = []
        evens = []
        evens_target = []
        for i in range(len(nums)):
            if nums[i]%2:
                odds.append(nums[i])
            else:
                evens.append(nums[i])
                
            if target[i]%2:
                odds_target.append(target[i])
            else:
                evens_target.append(target[i])
                
        return solve(odds, odds_target) + solve(evens, evens_target)

        