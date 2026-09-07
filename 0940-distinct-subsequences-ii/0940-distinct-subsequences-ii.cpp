class Solution {
public:
    int distinctSubseqII(string s) {
        unordered_set<string> se;
        const int mod = 1e9+7;
        int n = s.size();

        vector<int> dp( n+1 , 0 );
        vector<int>last( 26 , -1 );
        dp[0]=1;
        for(int i=1;i<=n;i++){
            int k = dp[i-1];
            if(last[s[i-1]-'a']==-1){
                dp[i]=(int)(2LL*k)%mod;
            }
            else{
                dp[i]=(int)((2LL*k - dp[last[s[i-1]-'a']] +mod)%mod);
            }
            last[s[i-1]-'a']=i-1;
        }
        return (dp[n] -1+mod)%mod;

    }
};