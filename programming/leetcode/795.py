class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        root = 0
        for row in range(n-1, 0, -1):
            nodes = (2**row)

            if k > nodes//2: 
                k -= nodes//2
                root = 1 - root
                
                
        return root