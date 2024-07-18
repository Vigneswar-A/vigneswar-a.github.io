class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        rem=0
        for i in range(1,K+1):          
            if (rem:=(rem*10+1)%K)==0:return i
        return -1
        