class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        near,far = 0,0
        d = {}
        ans = 0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1

            while len(d)>k:
                d[nums[near]]-=1
                if d[nums[near]]==0:
                    d.pop(nums[near])
                near+=1
                far = near
                
            while d[nums[near]]>1:
                d[nums[near]]-=1
                near+=1

            if len(d)==k:
                ans+=near-far+1
        return ans
        