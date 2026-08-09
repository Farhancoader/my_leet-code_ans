class Solution {
public:
    vector<int> parent;
    vector<long long> depth;

    long long getDepth(int u) {
        if (depth[u] != -1)
            return depth[u];

        return depth[u] = getDepth(parent[u]) + 1;
    }

    long long weightedSum(vector<int>& p, vector<int>& nums) {
        int n = nums.size();

        if (n == 0)
            return 0;

        parent = p;
        depth.assign(n, -1);

        depth[0] = 1;

        int h = 1;
        long long s = nums[0];
        long long diff = -1LL * nums[0];

        for (int i = 1; i < n; i++) {
            long long d = getDepth(i);

            h = max(h, (int)d);
            diff -= 1LL * nums[i] * d;
            s += nums[i];
        }

        return s * (h + 1LL) + diff;
    }
};