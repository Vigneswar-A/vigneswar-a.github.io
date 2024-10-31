class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
        if (k//(n-1))%2 == 0:
            return k%(n-1)
        else:
            return n-k%(n-1)-1
        