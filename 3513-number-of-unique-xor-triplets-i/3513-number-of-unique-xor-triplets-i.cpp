#include <bits/stdc++.h>
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        return n>=3?1<<(int)ceil(log2(n+1)):n;
        
    }
};