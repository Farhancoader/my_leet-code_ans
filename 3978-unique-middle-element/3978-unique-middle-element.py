class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        half = len(nums)//2
        for i in range(len(nums)):
            if i==half:
                continue
            if nums[i]==nums[half]:
                return False
        return True

        