class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix={0:-1}
        cum_sum=0
        rem=0
        
        for i,n in enumerate(nums):
            
            cum_sum+=n      
            
            if (rem:=cum_sum%k) in prefix:
                if i-prefix[rem]>1:
                    return True
                continue
            prefix[rem]=i              
                    
        return False
            