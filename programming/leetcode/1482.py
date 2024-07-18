from collections import Counter
from itertools import accumulate
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        X=sorted((C:=Counter(nums)).items())
        Y=dict((i,j) for i,j in accumulate(X,lambda A,B:(B[0],A[1]+B[1])))
        return [Y[i]-C[i] for i in nums]

            
        
        

        
        