class Solution {
public:
    int n = 1e5;
    vector<bool> dp;
    Solution(){
        dp.resize(n+1);
    for(int i=1;i<n+1;i++){
        long long r = sqrt(i);
        if(r*r==i){
            dp[i]=true;
            continue;
        }
        for(int j=1;j<=r;j++){
            if(!dp[i-j*j]){
                dp[i]=true;
                break;
                }
        }
    }
    }
    bool winnerSquareGame(int N) {
        return dp[N];
    }
};