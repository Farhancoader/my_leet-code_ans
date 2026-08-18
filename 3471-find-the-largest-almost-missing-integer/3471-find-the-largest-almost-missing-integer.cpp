class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        if(k==nums.size())return *max_element(nums.begin(),nums.end());
        if (k == 1) {
            unordered_map<int, int> freq;

            for (int x : nums)
                freq[x]++;

            int ans = -1;

            for (int x : nums) {
                if (freq[x] == 1)
                    ans = max(ans, x);
            }

            return ans;
        }
        int num2=nums[nums.size()-1],num1=nums[0];
        if(num1==num2)return -1;
        for(auto it=nums.begin()+1;it<nums.end()-1;it++){
            if(num1==-1 && num2==-1)break;
            if(*it==num1)num1=-1;
            else if(*it==num2)num2=-1;
        }
        return max(num1,num2);
    }
};