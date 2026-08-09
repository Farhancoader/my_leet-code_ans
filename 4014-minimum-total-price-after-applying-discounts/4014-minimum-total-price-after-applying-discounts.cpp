class Solution {
public:
    double minPrice(vector<int>& prices, vector<int>& dis) {
        sort(prices.rbegin(),prices.rend());
        int i=0,j=0;
        sort(dis.rbegin(),dis.rend());
        double ans = 0;
        while(i<prices.size() && j<dis.size()){
            ans +=prices[i++]*(100-dis[j++])/100.0;
        }
        while(i<prices.size())ans+=prices[i++];
        return ans;
    }
};