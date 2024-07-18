class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        arr = [*range(n)]
        
        arr = [arr[((n+i-1) if i%2 else i) // 2] for i in range(n)]
        
        count = 1
        while arr != list(range(n)):
            arr = [arr[((n+i-1) if i%2 else i) // 2] for i in range(n)]
            count += 1
            
        return count
            