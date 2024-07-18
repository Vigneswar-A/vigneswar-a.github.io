class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        res = 0
        stack = []
        
        for i in range(n+1):
            while stack and (i == n or arr[i] <= arr[stack[-1]]):
                smallest = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i           
                res += (smallest-left)*(right-smallest)*arr[smallest]
            
            stack.append(i)
            
        return res%(10**9 + 7)
            
            
            
                
        