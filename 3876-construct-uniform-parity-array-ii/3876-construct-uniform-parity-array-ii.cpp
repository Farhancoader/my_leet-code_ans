class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        bool has_odd=false;
        int mina = INT_MAX;
        for(int num:nums1){
            if(num&1)has_odd=true;
            mina = min(mina,num);
        }
        if(!has_odd)return true;
        return mina&1;
    }
};