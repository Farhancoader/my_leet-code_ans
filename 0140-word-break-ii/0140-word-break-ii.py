class Solution:
    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        n = len(s)
        words = set(words)
        dp = {}
        def dfs(i):
            if i==n:
                return [""]
            if i in dp:
                return dp[i]

            res = []
            for j in range(i,n):
                w = s[i:j+1]
                if w not in words:
                    continue
                sentences = dfs(j+1)
                for substr in sentences:
                    if substr:
                        res.append(w+" "+substr)
                    else:
                        res.append(w)
            dp[i]=res
            return res
        return dfs(0)
