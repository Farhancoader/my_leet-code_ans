class Solution {
public:
    string stoneGameIII(vector<int>& stones) {
        int n = stones.size();
        vector<long long> dp(n + 1, 0);  // dp[i] = max score diff from position i
        
        // Process from right to left
        for (int i = n - 1; i >= 0; i--) {
            long long curr = 0;
            dp[i] = LLONG_MIN;
            
            for (int k = 0; k < 3 && i + k < n; k++) {
                curr += stones[i + k];
                dp[i] = max(dp[i], curr - dp[i + k + 1]);
            }
        }
        
        long long ans = dp[0];
        if (ans > 0) return "Alice";
        else if (ans < 0) return "Bob";
        return "Tie";
    }
};