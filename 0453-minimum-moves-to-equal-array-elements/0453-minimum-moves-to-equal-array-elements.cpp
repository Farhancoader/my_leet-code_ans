class Solution {
public:
    int minMoves(vector<int>& nums) {
        int min = ranges::min(nums),sum = 0;
        for(int x :nums)sum+=x;
        return sum-min*nums.size();
    }
};