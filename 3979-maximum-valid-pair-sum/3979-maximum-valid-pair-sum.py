class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maxa = float("-inf")
        leftmax = float("-inf")

        for curr in range(k,len(nums)):
            element = nums[curr]
            leftmax = max(leftmax,nums[curr-k])
            maxa = max(maxa,element+leftmax)
        return maxa
