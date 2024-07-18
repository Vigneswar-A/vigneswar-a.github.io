class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg,pos=[],[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        neg.sort()
        for i in range(k):
            if neg:
                pos.append(-neg.pop(0))
                k-=1
            else:
                break
        
        return sum(pos+neg)-2*min(pos)*(k%2)
            
                