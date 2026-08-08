from collections import defaultdict
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:

        class fenwick():
            def __init__(self,n):
                self.bit = [0]*(n+1)
            def add(self,i,val):
                while i<len(self.bit):
                    self.bit[i]+=val
                    i+=i&-i

            def query(self,i):
                res = 0
                while i>0:
                    res+=self.bit[i]
                    i-=i&-i
                return res
        n = len(nums)
        def upperbound(arr,target):
            lo,high = 0,len(arr)-1
            ans = len(arr)
            while lo<=high:
                mid = (lo+high)//2
                if arr[mid]>target:
                    high=mid-1
                    ans = mid
                else:
                    lo = mid+1
            return ans
        pref = [(0,0)]
        odd = 0
        score = 0
        for x in nums:
            if x&1:
                odd+=1
                score+=a
            else:
                score-=b
            pref.append((odd,score))
        values = sorted(set(s for _,s in pref))
        pos_map = {v:i+1 for i,v in enumerate(values)}
        groups = defaultdict(list)
        for o,s in pref:
            groups[o].append(s)
        bit = fenwick(len(values))
        ans = 0
        for o in sorted(groups):
            for s in groups[o]:
                idx = upperbound(values,s)
                ans +=bit.query(idx)

            for s in groups[o]:
                bit.add(pos_map[s],1)
        return ans
                
            
        