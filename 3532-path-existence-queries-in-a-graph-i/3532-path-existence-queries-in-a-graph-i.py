class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        par = [i for i in range(len(nums))]
        def find(x):
            if x !=par[x]:
                par[x]=find(par[x])
            return par[x]
        def union(x,y):
            px,py = find(x),find(y)
            par[py]=px
        for i in range(n-1):
            if nums[i+1]-nums[i]<=maxDiff:
                union(i,i+1)
        ans = []
        for u,v in queries:
            if par[u]==par[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        

        