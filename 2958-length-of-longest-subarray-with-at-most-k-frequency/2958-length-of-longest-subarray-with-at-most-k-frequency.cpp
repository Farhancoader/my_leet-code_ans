class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int maxa = 0,curr = 0;
        int left = 0, n = nums.size();
        for(int i=0;i<n;i++){
            mp[nums[i]]++;
            while(mp[nums[i]]>k && left<n){
                mp[nums[left++]]--;
                curr--;
            }
            maxa = max(maxa,++curr);
        }
        return maxa;
    }
};