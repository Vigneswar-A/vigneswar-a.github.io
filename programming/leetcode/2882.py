class Solution {
public:
    int numberOfWays(int n, int x) {
        map<pair<int, int>, int> memo;
        return dp(0, 1, x, memo, n);
    }
    
    int dp(int total, int i, int x, map<pair<int, int>, int> &memo, int n)
    {
        const auto &key = make_pair(total, i);
        if (memo.find(key) != memo.end())
            return memo[key];
        
        if (total == n)
            return 1;
        
        if ((int)pow(i, x) + total > n)
            return 0;
        
        memo[make_pair(total, i)] = (dp(total+pow(i, x), i+1, x, memo, n) + dp(total, i+1, x, memo, n))%(1000000007);
        return memo[make_pair(total, i)];
    }
};