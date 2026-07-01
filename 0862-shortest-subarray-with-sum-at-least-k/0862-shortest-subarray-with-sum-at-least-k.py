from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        res = float("inf")
        currsum=0
        for r in range(len(nums)):
            currsum+=nums[r]
            if currsum>=k:
                res = min(res,r+1)
            while q and currsum-q[0][0]>=k:
                val,idx=q.popleft()
                res = min(res,r-idx)

            while q and q[-1][0]>currsum:
                q.pop()
            q.append((currsum,r))
        return res if res!=float("inf") else -1