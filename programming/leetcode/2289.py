class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        x = Counter(nums[1::2]).most_common(2)
        y = Counter(nums[::2]).most_common(2)
        res = 0
        
        if x[0][0] != y[0][0]:
            res = x[0][1] + y[0][1] 
        elif len(x) > 1 or len(y) > 1:
            if len(x) > 1:
                res = max(x[1][1]+y[0][1], res)
            if len(y) > 1:
                res = max(x[0][1]+y[1][1], res)
        else:
            return len(nums) // 2               
            
        return len(nums) - res
        
        
        