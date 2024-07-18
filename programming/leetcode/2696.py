class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        
        def dp(i=0, arr=[]):
            
                

            res = 1
           
            for j in range(i+1, len(nums)):
                if nums[j]-k in arr:
                    continue
                res += dp(j, arr+[nums[j]])
            return res
        
        return sum(dp(i, [nums[i]]) for i in range(len(nums)))
                
            
            
        
        