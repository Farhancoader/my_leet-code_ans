class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        sort(nums1.begin(),nums1.end());
        int first_odd=INT_MAX,first_even=INT_MAX;

        for(int i=0;i<nums1.size();i++){
            if(first_odd!=INT_MAX && first_even!=INT_MAX)break;
            if(nums1[i]&1 && first_odd==INT_MAX)first_odd=i;
            if(!(nums1[i]&1) && first_even==INT_MAX)first_even=i;
        }
        if(first_odd==INT_MAX || first_even==INT_MAX)return true;
        if(first_odd<first_even)return true;
        return false;
    }
};