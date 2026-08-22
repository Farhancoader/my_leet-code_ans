class Solution {
public:
    bool checkDivisibility(int n) {
        int digitsum =0,m = n;
        int product = 1;
        while(n){
            int curr = n%10;
            n = n/10;
            digitsum+=curr;
            product*=curr;
        }
        if(digitsum==0 && product==0)return false;
        cout<<m%(product+digitsum)<<endl;
        return (!(bool)(m%(product+digitsum)));

    }
};