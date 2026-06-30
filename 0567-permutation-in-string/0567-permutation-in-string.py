from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        r = 0
        l = 0
        window = Counter(s2[:len(s1)])
        if window==need:
            return True
        m,n = len(s1),len(s2)
        for r in range(m,n):
            window[s2[r]]+=1
            window[s2[l]]-=1
            if window[s2[l]]==0:
                window.pop(s2[l])
            l+=1
            if window==need:
                return True
        return False