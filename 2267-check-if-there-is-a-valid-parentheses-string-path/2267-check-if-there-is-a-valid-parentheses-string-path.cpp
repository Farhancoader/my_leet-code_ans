class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int n=grid.size(),m =grid[0].size();
        deque<vector<int>> q;
        vector<vector<unordered_set<int>>> mp(n, vector<unordered_set<int>> (m));
        mp[0][0].insert(converter(grid[0][0]));
        q.push_back({converter(grid[0][0]),0,0});

        vector<pair<int,int>> dirs = {{1,0},{0,1}};
        while(!q.empty()){
            vector<int> curr = q.front();
            int val =curr[0],r=curr[1],c=curr[2];
            int rem = n-r-1 + m-c-1;
            q.pop_front();
            if(val<0 || val>rem)continue;
            if(r==n-1 && c==m-1 && val==0)return true;
            for(auto [dr,dc]:dirs){
                int nr = r+dr, nc = c+dc;
                if(nr<n && nc<m){
                    int new_val=val+converter(grid[nr][nc]);
                    if(mp[nr][nc].find(new_val)!=mp[nr][nc].end())continue;
                    mp[nr][nc].insert(new_val);
                    q.push_back({new_val,nr,nc});
                    }
            }

        }
        return false;
    }
    int converter(char c){return (c=='('?1:-1);}
};