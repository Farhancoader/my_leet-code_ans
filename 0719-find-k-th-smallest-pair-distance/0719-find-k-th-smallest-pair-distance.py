class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def count(k):
            l = 0
            ans = 0
            for r in range(len(nums)):
                while nums[r]-nums[l]>k:
                    l+=1
                ans+=r-l
            return ans
        l,r = 0,max(nums)
        while l<r:
            mid = (l+r)//2
            pairs = count(mid)
            if pairs>=k:
                r=mid
            else:
                l=mid+1
        return r
                    
        