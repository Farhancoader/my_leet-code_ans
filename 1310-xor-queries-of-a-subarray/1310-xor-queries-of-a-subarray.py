class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1]^num)
        ans = []
        for l,r in queries:
            ans.append(prefix[r+1]^prefix[l])
        return ans
        