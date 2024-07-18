class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        end = 0
        for i in range(n):
            end |= (1 << i)
        
        total = sum(nums)
        if total%k != 0:
            return False
        
        subsum = total//k
        @cache
        def dp(bitmask=0, subs=1, total=0):
            if subs > k or total > subsum:
                return False
            
            if bitmask == end and total == subsum:
                return True
            
            for i in range(n):      
                if bitmask&(1<<i) == 0:
                    if total+nums[i]==subsum and dp(bitmask|(1<<i), subs+1, 0):
                        return True
                    elif dp(bitmask|(1<<i), subs, total+nums[i]):
                        return True
                        
            return False
            
        return dp()
                            
        