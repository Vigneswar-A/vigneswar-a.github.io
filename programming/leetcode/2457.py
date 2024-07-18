class Solution {
public:
    
    int countSpecialNumbers(int a) {
        int digits = log10(a)+1;
        if(a<=10) return a;
        int avail = 9,ans=0;
        int one = a%10;
        for(int i=0;i<digits-1;i++)
        {
            ans+=avail;
            avail*=(9-i);
        }
        string z = to_string(a);
        reverse(z.begin(),z.end());
        long long n = stoll(z);
        int dig=log10(n)+1;
        dig = digits-dig;
        set<int> s;
        cout<<ans<<'\n';
        for(int i=0;n;i++)
        {
            int up = n%10;
            int cnt=up;
            if(i==0) cnt--;
            
            for(int x:s){
                if(x<up)cnt--;
            }
            int t=9-i;
            int b=1;
            for(int j=i+1;j<digits;j++)
            {
                b*=t;
                t--;
            }
            n/=10;
            ans+=cnt*b;   
            
            int a = s.size();
            s.insert(up);
            if(s.size()==a) return ans;
            
                         
            cout<<ans<<"\n\n";
        }
        
        return ans+(dig<=1);
    }
};