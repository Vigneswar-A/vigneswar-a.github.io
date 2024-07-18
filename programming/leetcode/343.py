class Solution {
public:
    int integerBreak(int n) {
        if (n <= 3)
            return n-1;
        int dp[52] = {0};
        return top_down(n, dp);
    }
    
    int top_down(int n, int dp[]){
        if(dp[n] != 0)
            return dp[n];
        
        dp[n] = n;
        for(int j = 1; j <= n/2; j++)
            dp[n] = max(dp[n], top_down(j, dp)*top_down(n-j, dp));
        
        return dp[n];
    }
};