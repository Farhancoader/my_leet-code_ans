class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1]*n
        for i in range(2*n-1,-1,-1):
            pos = i%n if i>=n else i
            while stack and nums[pos]>=stack[-1]:
                stack.pop()
            ans[pos]=stack[-1] if stack else -1
            stack.append(nums[pos])
        return ans
            
