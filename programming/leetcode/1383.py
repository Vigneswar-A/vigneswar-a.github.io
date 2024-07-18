class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        res = 0
        
        for i in range(1, 101):
            for j in range(i, 101):
                for k in range(j, 101):
                    sum = i+j+k
                    if ((sum%i == 0) + (sum%j == 0) + (sum%k == 0) == 1):
                        if i == j != k and counts[i]:
                            res += (counts[i]-1)*(counts[j])*(counts[k])//2
                        elif i != j == k and counts[j]:
                            res += (counts[i])*(counts[j]-1)*(counts[k])//2
                        elif i != j and j != k and i != k:
                            res += (counts[i]*counts[j]*counts[k])
                        
                        
        return int(res)*6
                        