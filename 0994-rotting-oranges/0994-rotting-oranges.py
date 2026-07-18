from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()

        Rows , Cols = len(grid), len(grid[0])

        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append([i,j])
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh>0:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr ,dc in dirs:
                    row, col = r+dr, c+dc

                    if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]!=1:
                        continue
                    else:
                        grid[row][col] =2
                        q.append((row,col))
                        fresh -=1
            time +=1

        if fresh>0:
            return -1
        return time 



        