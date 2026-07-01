from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()
        visit = set()
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    grid[i][j]=0
                    visit.add((i,j))
                    q.append((i,j,0))
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            i,j,val = q.popleft()
            grid[i][j]=val
            for dr,dc in dirs:
                nr,nc = i+dr,j+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    q.append((nr,nc,val+1))
        heap = [(-grid[0][0],0,0)]
        mina = float("inf")
        visit = set()
        while heap:
            val,r,c = heapq.heappop(heap)
            if r==n-1 and c==m-1:
                return -val
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    heapq.heappush(heap,(-min(-val,grid[nr][nc]),nr,nc))
        return 0

            
        


        