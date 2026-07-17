class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = {}
        rows,cols = len(grid),len(grid[0])
        def dfs(r,c1,c2):
            if not (0<=c1<cols and 0<=c2<cols):
                return float("-inf")
            if (r,c1,c2) in dp:
                return dp[(r,c1,c2)]
            cherries = grid[r][c1]
            if c1!=c2:
                cherries+=grid[r][c2]
            if r==rows-1:
                return cherries
            best = 0
            for dc1 in (-1,0,1):
                for dc2 in (-1,0,1):
                    best = max(best,dfs(r+1,c1+dc1,c2+dc2))
            dp[(r,c1,c2)]=cherries+best
            return dp[(r,c1,c2)]
        return dfs(0,0,cols-1)
