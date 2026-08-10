const int n = 1e5;
    int dp[n+1];
    auto init  = [](){
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
    return 0;
    }();
class Solution {
public:
    bool winnerSquareGame(int N) {
        return dp[N];
    }
};