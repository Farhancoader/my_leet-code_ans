class Solution {
public:
    multiset<long long> lo,high;
    long long sumlo=0,sumhi=0;
    int target;
    void balance(){
       int desired = min(target, (int)(lo.size() + high.size()));

    while (lo.size() > desired) {
        auto it = prev(lo.end());
        long long v = *it;

        lo.erase(it);
        sumlo -= v;

        high.insert(v);
        sumhi += v;
    }

    while (lo.size() < desired) {
        auto it = high.begin();
        long long v = *it;

        high.erase(it);
        sumhi -= v;

        lo.insert(v);
        sumlo += v;
    }
}

    void add(long long v){
        if(lo.empty() || v<=*lo.rbegin()){
            lo.insert(v);
            sumlo+=v;
        }
        else{
            high.insert(v);
            sumhi+=v;
        }
        balance();
    }
    void remove(long long v){
        auto it = lo.find(v);
        if(it!=lo.end()){
            auto v = *it;
            lo.erase(it);
            sumlo-=v;
        }
        else{
            auto it = high.find(v);
            auto v = *it;
            high.erase(it);
            sumhi-=v;
        }
        balance();
    }
    long long getcost(){
        long long median = *(lo.rbegin());
        return sumhi-sumlo+median*(1LL*lo.size()-high.size());
    }
    long long minOperations(vector<int>& nums, int x, int k) {
        lo.clear();
        high.clear();
        sumlo = sumhi = 0;

        target = (x + 1) / 2;
        int n = nums.size();
        int m = n-x+1;
        vector<long long>cost(m);
        for(int i =0;i<x;i++){
            add(nums[i]);
        }
        cost[0]=getcost();
        for(int i =x;i<n;i++){
            remove(nums[i-x]);
            add(nums[i]);
            cost[i-x+1]=getcost();
        }
        vector<vector<long long>>dp(m+1,vector<long long>(k+1,LLONG_MAX/4));
        for(int i =0;i<=m;i++){
            dp[i][0]=0;
        }
        for(int i =1;i<=m;i++){
            for(int j=1;j<k+1;j++){
                dp[i][j] =min(dp[i-1][j],cost[i-1]+dp[max(0,i-x)][j-1]);
            }
        }
        return dp[m][k];
    }
};