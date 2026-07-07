class Solution:
    def sumAndMultiply(self, n: int) -> int:
        k = str(n)
        s = ""
        su=0
        for c in k:
            if c!="0":
                s+=c
            su+=int(c)
        return su*int(s) if s else 0 
        