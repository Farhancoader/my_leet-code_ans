class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        n = len(c)
        if k==n:
            return sum(c)
        window = n-k
        curr = sum(c[:window])
        mn = curr
        for i in range(window,n):
            curr+=c[i]
            curr-=c[i-window]
            mn = min(curr,mn)
        return sum(c)-mn
        