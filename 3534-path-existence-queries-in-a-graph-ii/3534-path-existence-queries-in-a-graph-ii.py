class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i],i) for i in range(n))
        pos = [0]*n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i
        grps = [0]*n
        curr = 0
        for i in range(1,n):
            if arr[i][0]-arr[i-1][0]>maxDiff:
                curr+=1
            grps[i]=curr
        nxt = [0]*n
        def findnext(i):
            low = i
            high = n-1
            target = arr[i][0]+maxDiff
            ans = i
            while low<=high:
                mid = (low+high)//2
                if arr[mid][0]<=target:
                    ans = mid
                    low=mid+1
                else:
                    high = mid-1
            return ans

        for i in range(n):
            nxt[i]=findnext(i)

        log = n.bit_length()
        up = [[0]*log for i in range(n)]

        for i in range(n):
            up[i][0]=nxt[i]

        for k in range(1,log):
            for i in range(n):
                up[i][k]=up[up[i][k-1]][k-1]
        ans = []
        for u,v in queries:
            l = pos[u]
            r = pos[v]
            if l > r:
                l, r = r, l
            if grps[l]!=grps[r]:
                ans.append(-1)
                continue
            if l==r:
                ans.append(0)
                continue
            curr=l
            jumps = 0
            for k in range(log-1,-1,-1):
                if up[curr][k]<r:
                    jumps += 1<<k
                    curr=up[curr][k]
            ans.append(jumps+1)
        return ans




