class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posdiag = set()
        negdiag = set()
        board = [['.']*n for _ in range(n)]
        ans = []

        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            for c in range(n):
                if c in cols or r-c in negdiag or r+c in posdiag:
                    continue

                board[r][c] = 'Q'
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                backtrack(r+1)

                board[r][c] = '.'
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)

        backtrack(0)
        return ans

        
