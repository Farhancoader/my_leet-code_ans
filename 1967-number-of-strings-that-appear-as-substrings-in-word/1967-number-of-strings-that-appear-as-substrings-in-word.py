class node:
    def __init__(self):
        self.children = {}
        self.ids = []
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        root = node()
        for idx,pattern in enumerate(patterns):
            curr = root
            for ch in pattern:
                if ch not in curr.children:
                    curr.children[ch]=node()
                curr = curr.children[ch]
            curr.ids.append(idx)
        found = [False]*len(patterns)
        for i in range(len(word)):
            curr,j = root,i
            while j<len(word) and word[j] in curr.children:
                curr=curr.children[word[j]]
                for idx in curr.ids:
                    found[idx]=True
                j+=1
        return sum(found)

        