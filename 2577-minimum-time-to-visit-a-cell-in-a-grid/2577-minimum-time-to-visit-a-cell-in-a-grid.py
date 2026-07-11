from heapq import heappush,heappop
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        n,m = len(grid),len(grid[0])
        visited = set()
        visited.add((0,0))
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        heap = [(grid[0][0],0,0)]
        while heap:
            curr_time,r,c = heappop(heap)
            if r==n-1 and c==m-1:
                return curr_time
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited:
                    wait = 1 if (abs(grid[nr][nc]-curr_time))&1==0 else 0
                    new_time = max(curr_time+1,grid[nr][nc]+wait)
                    heappush(heap,(new_time,nr,nc))
                    visited.add((nr,nc))
        return -1 