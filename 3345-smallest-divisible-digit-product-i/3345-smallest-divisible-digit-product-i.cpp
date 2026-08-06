class Solution {
public:
    int productnum(int i){
        int ans = 1;
        while(i>0){
            int curr = i%10;
            if(curr==0)return 0;
            i=i/10;
            ans*=curr;
        }
        return ans;
    }
    int smallestNumber(int n, int t) {
        while(true){
        if(!(productnum(n)%t))return n;
        else n++;
        }
    }
};