class Solution {
public:
    bool predictTheWinner(vector<int>& nums) {
        function<long long(int,int)> score = [&](int i,int j){
            if(i>j){
                return 0LL;
            }
            return (max(nums[i]-score(i+1,j),nums[j]-score(i,j-1)));
        };
        return score(0,nums.size()-1)>=0;
    }
};