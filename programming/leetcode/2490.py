class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        
        n = len(books)
        dp = [0]*n
        ans = 0
        stack = []
        
        for i in range(n):
            while stack and books[stack[-1]] >= books[i]-i+stack[-1]:
                stack.pop()
                
            if stack:
                dp[i] = dp[stack[-1]] + books[i]*(books[i]+1)//2 - (books[i]-(i-stack[-1]-1))*(books[i]-(i-stack[-1]))//2
            else:
                dp[i] = books[i]*(books[i]+1)//2 - ((books[i]-i-1)*(books[i]-i)//2 if books[i]-1 > i else 0)
                
            stack.append(i)
            ans = max(ans, dp[i])
            
        return ans
                
        
        
        
                
            