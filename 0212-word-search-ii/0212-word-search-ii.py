class node():
    def __init__(self):
        self.children = {}
        self.end = False
    def addword(self,word: str):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=node()
            curr = curr.children[c]
        curr.end = True 
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = node()
        row,col = len(board),len(board[0])
        res,visit = set(),set()
        for word in words:
            root.addword(word)
        def dfs(r,c,node,word):
            if r<0 or c<0 or r>=row or c>=col or (r,c) in visit or board[r][c] not in node.children:
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.end:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for i in range(row):
            for j in range(col):
                dfs(i,j,root,"")
        return list(res)

