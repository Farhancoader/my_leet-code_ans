class Solution {
public:
    long long check(vector<int> &coins,long long m){
        int n = coins.size();
        long long curr = 0;
        for(int mask = 1;mask<1<<n;mask++){
            long long l = 1;
            for(int i=0;i<n;i++){
                if(mask &(1<<i)){
                    l = lcm(l, (long long)coins[i]);
                }

            }
            if(__builtin_popcount(mask)&1)curr+=m/l;
            else curr-=m/l;
        }
        return curr;
    }
    long long findKthSmallest(vector<int>& coins, int k) {
        long long low = 1LL,high = 1LL*(*min_element(coins.begin(),coins.end()))*k;

        while(low<=high){
            long long mid = low+(high-low)/2;
            long long val = check(coins,mid);

            if(val>=k)high=mid-1;
            else low = mid+1;
    }
        return low;
        }
    };