class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        unordered_map<int,vector<int>> mp;
        int m =invocations.size();
        for(int i=0;i<m;i++){
            int u = invocations[i][0],v = invocations[i][1];
            mp[u].push_back(v);
        }
        vector<bool>sus(n+1,false);
        queue<int>q;
        q.push(k);
        sus[k]=true;
        while(!q.empty()){
            int node = q.front();
            q.pop();
            for(int newnode:mp[node]){
                if(!sus[newnode]){
                    sus[newnode]=true;
                    q.push(newnode);
                }
            }
        }
        for(auto inv:invocations){
            if (!sus[inv[0]] && sus[inv[1]]) {
                vector<int> result(n);
                iota(result.begin(), result.end(), 0);
                return result;
            }
        }
        vector<int> result;
        for (int i = 0; i < n; i++) {
            if (!sus[i]) {
                result.push_back(i);
            }
        }
        return result;
        
    }
};