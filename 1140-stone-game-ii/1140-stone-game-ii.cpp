class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; i--)
            suffix[i] = suffix[i + 1] + piles[i];

        vector<vector<int>> dp(n, vector<int>(n + 1, -1));

        function<int(int,int)> dfs = [&](int i,int x)->int{
            if(i==n)return 0;
            if(dp[i][x]!=-1)return dp[i][x];

            for(int j = i;j<i+2*x && j<n;j++){
                dp[i][x] = max(dp[i][x],suffix[i]-dfs(j+1,max(x,j-i+1)));
            }
            return dp[i][x];
            };
        return dfs(0,1);
        }
};