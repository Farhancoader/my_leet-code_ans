class Solution:
    def removeCoveredIntervals(self, times: List[List[int]]) -> int:
        times.sort(key=lambda x:(x[0],-x[-1]))
        ans = 1
        prev = times[0][1]
        for start,end in times:
            if prev>=end:
                continue
            else:
                ans+=1
            prev = end
        return ans
         
        