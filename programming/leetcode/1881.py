class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)//2
        first_half = nums[:n]
        second_half = nums[n:]
        
        def sums(nums, res, i=0, total=0):
            if i == len(nums):
                res.add(total)
                return res
            sums(nums, res, i+1, total+nums[i])
            sums(nums, res, i+1, total)
            return res
            
        second_sums = sorted(sums(second_half, set()))
        res = inf
        m = len(second_sums)
        for i in sums(first_half, set()):
            target = goal-i         
            j = bisect.bisect(second_sums, target)
            if j >= 0:
                res = min(res, abs(target-second_sums[j-1]))
            if j <= m-1:
                res = min(res, abs(target-second_sums[j]))
            
        return res
            