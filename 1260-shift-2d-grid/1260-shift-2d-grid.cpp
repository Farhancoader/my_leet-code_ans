class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> l(n*m,0);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                l[i*m+j]=grid[i][j];
            }
        }
        rotate(l.begin(),l.end()-(k%(n*m)),l.end());
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                grid[i][j]=l[i*m +j];
            }
        }
        return grid;
        
    }
};