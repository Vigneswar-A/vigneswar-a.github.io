class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        
        @cache
        def dp(i=0, odd=0):
            if i >= n:
                return odd
            return dp(i+1, odd^(arr[i]&1))+odd
        
        return sum(dp(i) for i in range(n))%1000000007
        
        
           
            
            
            
        