class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        """
        A = An + (N-1) D
        so,
        D = (An - A) / N-1
        """
        
        d = (arr[-1] - arr[0]) // (N := len(arr))
        
        for i in range(1 , N):
            if arr[i] - arr[i - 1] != d:
                return arr[0] + i * d
            
        return arr[0]
        
            
        
        
        