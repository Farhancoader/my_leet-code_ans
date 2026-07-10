class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ones = 0
        rows,cols = len(grid),len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    ones+=1
        visit = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c):
            nonlocal ones
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0 or (r,c) in visit:
                return
            visit.add((r,c))
            ones-=1
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit and grid[nr][nc]==1:
                    dfs(nr,nc)
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        return ones 
              
        