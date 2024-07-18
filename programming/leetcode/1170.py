class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n,m = len(str1),len(str2)
        dp = [['']*(m+1) for _ in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i]+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j], key = len)

        def solve(string):
            sub = deque(dp[0][0])
            temp = list(string)

            for i in range(len(temp)):
                if not sub:
                    break

                if sub[0] == temp[i]:
                    sub.popleft()
                    temp[i] = '#'
            return temp
         
        temp1 = [*solve(str1)]
        temp2 = [*solve(str2)] 
        sub = deque(dp[0][0])
        
        i = j = 0
        res = ''
        while i != len(temp1) or j != len(temp2):
            if i < len(temp1) and temp1[i] != '#':
                res += temp1[i]
                i += 1
            elif j < len(temp2) and temp2[j] != '#':
                res += temp2[j]
                j += 1
            elif sub:
                res += sub.popleft()
                i += 1
                j += 1
        return res
                

        
        
        
                
            