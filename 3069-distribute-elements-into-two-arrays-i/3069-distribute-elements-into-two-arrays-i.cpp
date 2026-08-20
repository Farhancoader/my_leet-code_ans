class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
       int first = nums[0];
       int second = nums[1];
       int n = nums.size();
       vector<int> arr1(1,nums[0]);
       vector<int> arr2(1,nums[1]);
       for(int i=2;i<n;i++){
        if(first>second){
            arr1.push_back(nums[i]);
            first=nums[i];
        }
        else{
            arr2.push_back(nums[i]);
            second=nums[i];
        }
       }
       arr1.insert(arr1.end(),arr2.begin(),arr2.end());
       return arr1; 
    }
};