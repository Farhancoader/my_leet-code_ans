class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& rs) {
        unordered_map<int,int> bits;

        for(auto &it:rs){
            if(it[1]==1 || it[1]==10)continue;
            if(bits.count(it[0]) == 0) bits[it[0]] = 7;
            if(it[1]>1 && it[1]<=5)bits[it[0]]&=6;
            if(it[1]>3 && it[1]<8)bits[it[0]]&=5;
            if(it[1]>5 && it[1]<10)bits[it[0]]&=3;   
        }
        int ans = 2 * (n - bits.size());
        for(auto [row,mask]:bits){
            if(mask==7)ans+=2;
            else if(mask>0)ans++;
        }
        return ans;
    }
};