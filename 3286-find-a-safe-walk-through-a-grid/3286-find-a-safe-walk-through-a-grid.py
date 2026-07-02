import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        heap=[(grid[0][0],0,0)]
        n,m = len(grid),len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visit = set((0,0))
        while heap:
            h,r,c = heapq.heappop(heap)
            print(h,r,c)
            if r==n-1 and c==m-1:
                return h<health
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    if grid[nr][nc]==1:
                        if h+1<health:
                            heapq.heappush(heap,(h+1,nr,nc))
                    else:
                        heapq.heappush(heap,(h,nr,nc))
        return False

            
        