class Solution {
public:
    int maxProduct(int n) {
        int firstmax=0,secondmax=0;
        while(n){
            bool flag = true;
            int digit = n%10;
            n = n/10;
            if(firstmax<=digit){
                secondmax=firstmax;
                firstmax = digit;
                flag = false;
            }
            if(flag)secondmax = max(secondmax,digit);
        }
        return firstmax*secondmax;
    }
};