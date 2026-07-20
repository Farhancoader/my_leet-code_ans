class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& v, int k) {
        deque<pair<int,vector<int>::iterator>> dq;
        for(auto it=v.begin();it<v.begin()+k;it++){

            while(!dq.empty() && dq.back().first<*it){

                dq.pop_back();
            }
            dq.push_back({*it,it});
        }

        vector<int> ans(v.size()-k+1,0);
        auto it2 = ans.begin();
        *it2 = dq.front().first;
        it2++;
        for(auto it = v.begin()+k;it<v.end();it++){
            
            while(!dq.empty() && dq.front().second+k<it){
                dq.pop_front();
            }

            while(!dq.empty() && dq.back().first<*(it)){
                dq.pop_back();
            }
            dq.push_back({*it,it});
            *it2=dq.front().first;
            it2++;
        }
        return ans;
        
    }
};