#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int gcd(int a,int b){
        if(b==0)return a;
        return gcd(b,a%b);
    }
public:
    int findGCD(vector<int>& nums) {
        return gcd(*max_element(nums.begin(),nums.end()),*min_element(nums.begin(),nums.end()));
    }
};