class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int mina=INT_MAX,maxa=INT_MIN;
        int minpos=0,maxpos=0;
        int n = nums.size();
        for(int i=0;i<n;i++){
            if(mina>nums[i]){
                mina=nums[i];minpos=i;
            }
            if(maxa<nums[i]){
                maxa=nums[i];maxpos=i;
            }
        }
        int left = min(minpos,maxpos);
        int right = max(minpos,maxpos);
        return min({n-left,right+1,left+n-right+1});
    }
};