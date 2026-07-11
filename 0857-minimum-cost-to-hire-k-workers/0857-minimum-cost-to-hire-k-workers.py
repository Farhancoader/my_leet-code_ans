from heapq import heappush,heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = []
        for i in  range(len(wage)):
            pairs.append([wage[i]/quality[i],quality[i]])
        pairs.sort()
        maxheap = []
        totalq,res = 0,float("inf")
        for rate,q in pairs:
            heappush(maxheap,-1*q)
            totalq+=q

            if len(maxheap)>k:
                q = -heappop(maxheap)
                totalq-=q

            if len(maxheap)==k:
                res = min(res,rate*totalq)

        return res