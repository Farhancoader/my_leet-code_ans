int lsb(int i){
    return i&-i;
}
class NumArray {
public:
    int n;
    vector<int> bits;
    vector<int>arr;
    NumArray(vector<int>& nums) {
        this->n = nums.size();
        this->bits.resize(n+1);
        this->arr=nums;
        for (int i = 0; i < n; i++) {
            bits[i + 1] = nums[i];
        }

        for (int i = 1; i <= n; i++) {
            int parent = i + lsb(i);

            if (parent <= n) {
                bits[parent] += bits[i];
            }
        }
    }
    
    void update(int index, int val) {
        int diff = val-arr[index];
        arr[index]=val;
        int i = index+1;
        while(i<=this->n){
            bits[i]+=diff;
            i+=lsb(i);
        }
    }
    int query(int i){
        int ans=0;
        while(i>0){
            ans+=bits[i];
            i-=lsb(i);
        }
        return ans;
    }
    
    int sumRange(int left, int right) {
        return query(right+1)-query(left);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */