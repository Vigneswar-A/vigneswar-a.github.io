class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:

        oddsum = evensum = 0
        odds = []
        evens = []

        for i in sorted(nums, reverse=1):
            if i%2:
                oddsum += i
                odds.append(oddsum)
            else:
                evensum += i
                evens.append(evensum)

        res = -1  
        print(odds, evens, k)
        if len(odds) >= k and odds[k-1]%2 == 0:     
            res = odds[k-1]
        
        if len(evens) >= k:
            res = max(res, evens[k-1])

        for i in range(k):
            if i < len(odds) and k-i-2 >= 0 and k-i-2 < len(evens) and odds[i]%2 == 0:
                res = max(res, odds[i] + evens[k-i-2])
        return res
                
