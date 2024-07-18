class Solution {
public:
    int findIntegers(int n) {
        return dp(1, n) + 1;
    }
    
    int dp(int num, int n){
        if (num > n)
            return 0;
        
        if (num&1)
            return 1 + dp(num << 1, n);
            
        return 1 + dp((num << 1) + 1, n) + dp(num << 1, n);
    }
    
};