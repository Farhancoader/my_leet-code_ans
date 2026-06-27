class node():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=node()
            curr = curr.children[c]
        curr.end=True

    def search(self, word: str) -> bool:
        def dfs(curr,i):
            if i==len(word):
                return curr.end
            c = word[i]
            if c==".":
                for child in curr.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            if c not in curr.children:
                return False

            return dfs(curr.children[c],i+1)
        return dfs(self.root,0)


            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)