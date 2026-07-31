class Solution {
public:
    int minimumPushes(string word) {
        vector<int> v(26,0);
        for(char c:word){
            v[c-'a']++;
        }
        sort(v.begin(),v.end());
        long long ans = 0;
        int mul = 0;
        for(int i=25;i>=0;i--){
            if(((25-i)%8)==0)mul++;
            ans+=v[i]*mul;
        }
        return ans;
        
    }
};