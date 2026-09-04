class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prev(n,nums[n-1]);
        for(int i=n-2;i>-1;i--){
            prev[i]=min(nums[i],prev[i+1]);
        }
        int currmax=INT_MIN;
        for(int i=0;i<n;i++){
            currmax=max(nums[i],currmax);
            int val = currmax-prev[i];
            if(val<=k)return i;
        }
        return -1;  

    }
};