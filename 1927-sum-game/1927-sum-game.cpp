class Solution {
public:
    bool sumGame(string s) {
        int n = s.size();
        long long leftsum=0,rightsum=0;
        int ql = 0,qr = 0;
        for(int i=0;i<n/2;i++){
            if(s[i]=='?')ql++;
            else leftsum+=s[i]-'0';
        }
        for(int i=n/2;i<n;i++){
            if(s[i]=='?')qr++;
            else rightsum+=s[i]-'0';
        }
        int act = qr-ql;
        if(act==0)return !(leftsum==rightsum);
       return  2 * (leftsum - rightsum) != 9 * (act);
    }
};