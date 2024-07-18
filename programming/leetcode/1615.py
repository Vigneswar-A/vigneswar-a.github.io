class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sums = []
        prefix = list(accumulate(nums)) + [0]
        
        for i in range(n):
            for j in range(i, n):
                sums.append(prefix[j]-prefix[i-1])
                
        sums.sort()
        
        return sum(sums[left-1:right])%(10**9 + 7)
        
        
       
        