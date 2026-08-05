class Solution {
public:
    string stoneGameIII(vector<int>& stones) {
        int n = stones.size();
        vector<long long> player(n,LLONG_MIN);
        auto dfs = [&](auto&& self,int i)->long long{
            if(i>=stones.size())return 0LL;

            if(player[i]!=LLONG_MIN)return player[i];
            long long curr = 0;
            for(int k=0;k<3;k++){
                if(i+k<n){
                    curr+=stones[i+k];
                    player[i]=max(player[i],curr-self(self,i+k+1));
                }
            }
            return player[i];
        };
        long long ans = dfs(dfs,0);
        if(ans>0)return "Alice";
        else if(ans<0)return "Bob";
        return "Tie";
        
    }
};