class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int>ch(26,0);
        int k=-1;
        for(char c:s){
            ch[c-'a']++;
        }
        string ans="";
        for(int i=0;i<26;i++){
            if(ch[i]&1){
                k = i;
            }
            ans+=string(ch[i]/2,char('a'+i));
        }
        if(k!=-1){
            ans+=string(1,'a'+k);
        }
        for(int i=25;i>=0;i--){
            ans+=string(ch[i]/2,char('a'+i));
        }
        return ans;
    }
};