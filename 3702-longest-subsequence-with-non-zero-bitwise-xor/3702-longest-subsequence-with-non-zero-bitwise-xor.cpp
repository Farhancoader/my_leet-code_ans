class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int xor_sum = 0,zcount = 0, n = nums.size();
        for(int num:nums){
            xor_sum^=num;
            if(num==0)zcount++;
        }
        if(xor_sum!=0)return n;
        if(zcount==n)return 0;
        return n-1;

        }
};