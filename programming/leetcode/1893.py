int max(int a, int b){
    if (a>b)
        return a;
    return b;
}
int solve(vector<int>& v)
{
    int n = 0, m = 0, k = 0, x = 0, count = 0, sum = 0, ans = 0;
    
    n = v.size();
    vector<int> kad1(n+2),kad2(n+2);

    int gl=0,lo=0;
    for(int i=0;i<n;i++)
    {
        lo = max(v[i],v[i]+lo);
        lo = max(lo,0LL);
        kad1[i+1] = lo;
    }
    //fv(kad1)

    lo = 0;
    for(int i=n-1;i>=0;i--)
    {
        lo = max({v[i],v[i]+lo});
        lo = max(lo,0LL);
        kad2[i+1] = lo;       
    }
   // fv(kad2)
    for(int i=1;i<=n;i++)
    {   
        ans = max(ans,v[i-1]*v[i-1]+kad1[i-1]+kad2[i+1]);
    }

    return ans;



}
class Solution {
public:
    int maxSumAfterOperation(vector<int>& nums) {
        return  solve(nums);
    }
};