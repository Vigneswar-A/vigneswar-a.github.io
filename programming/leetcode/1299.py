class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        cum_sum = 0
        max_sum = 0
        
        for i in arr:
            cum_sum = max(i, cum_sum + i)
            max_sum = max(max_sum, cum_sum) 
           
        res1 = max_sum
        for i in arr:
            cum_sum = max(i, cum_sum + i)
            max_sum = max(max_sum, cum_sum)
            
        res2 = max_sum
        for i in arr:
            cum_sum = max(i, cum_sum + i)
            max_sum = max(max_sum, cum_sum)
            
        return max(res1 + (max_sum-res2)*(k-1), res2 if k > 1 else res1)%1000000007
        