class Solution {
public:
    int josh(int n,int k){
        if(n==1)return 0;
        return (josh(n-1,k) +k)%n;
    }
    int findTheWinner(int n, int k) {
        return josh(n,k)+1;
    }
};