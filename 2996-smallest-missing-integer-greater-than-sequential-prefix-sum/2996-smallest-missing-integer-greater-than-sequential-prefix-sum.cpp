class Solution {
public:
    int missingInteger(vector<int>& nums) {
        unordered_set<int> s(nums.begin(),nums.end());
        int prefix_sum =nums[0];
        int i =1,n = nums.size();
        while(i<n && nums[i]==nums[i-1]+1){
            prefix_sum+=nums[i++];
        }
        while(s.find(prefix_sum)!=s.end())prefix_sum++;
        return prefix_sum;
    }
};