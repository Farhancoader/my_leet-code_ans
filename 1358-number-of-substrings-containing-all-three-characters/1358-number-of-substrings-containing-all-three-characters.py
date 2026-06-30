class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a":0,"b":0,"c":0}
        l = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]]+=1
            while count['a']>0 and count["b"]>0 and count["c"]>0:
                count[s[l]]-=1
                l+=1 
            ans+=l
        return ans