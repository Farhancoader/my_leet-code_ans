class Solution {
public:
    struct bitbuf{
        unsigned long long data[2];
        void init(){
            data[0]=1;
            data[1]=0;
        }
        void inc(){
            bool carry = (data[0]>>63) &1;
            data[0]<<=1;
            data[1]<<=1;
            if(carry)data[1]|=1;
        }
        void dec(){
            bool carry = data[1]&1;
            data[0]>>=1;
            data[1]>>=1;
            if(carry)data[0]|=(1ull<<63);
        }
        void shift(int d){
            if(d==1)inc();
            else dec();
        }
        void merge(bitbuf other){
            data[0]|=other.data[0];
            data[1]|=other.data[1];
        }
        bool contains_zero() {
            return data[0] & 1ULL;
        }
        void copy(const bitbuf& other) {
        data[0] = other.data[0];
        data[1] = other.data[1];
        }
    };
    bool hasValidPath(vector<vector<char>>& grid) {
        int R = grid.size(),C=grid[0].size();
        vector<vector<bitbuf>> dp(
            2,
            vector<bitbuf>(C)
        );

        auto val = [&](int r, int c) {
            return grid[r][c] == '(' ? 1 : -1;
        };

        dp[0][0].init();
        dp[0][0].shift(val(0,0));
        for(int c=1;c<C;c++){
            dp[0][c]=dp[0][c-1];
            dp[0][c].shift(val(0,c));
        } 
        for(int r = 1;r<R;r++){
            int curr = r&1;
            int prev = curr^1;
            dp[curr][0]=dp[prev][0];
            dp[curr][0].shift(val(r,0));
            for(int c = 1;c<C;c++){
                dp[curr][c]=dp[prev][c];
                dp[curr][c].merge(dp[curr][c-1]);
                dp[curr][c].shift(val(r,c));
            }
        }
        return dp[(R-1)&1][C-1].contains_zero();
    }
};