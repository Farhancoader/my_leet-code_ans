class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        int mina = INT_MAX;
        int maxa = INT_MIN;
        unordered_set<int> s;
        for(int num : nums){
            mina = min(mina,num);
            maxa = max(maxa,num);
            s.insert(num);
        }
        vector<int> ans;
        for(int i=mina+1;i<maxa;i++)if(s.find(i)==s.end())ans.push_back(i);
        return ans;
    }
};