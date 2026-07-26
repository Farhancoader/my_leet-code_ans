# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val>=max(left,right):
                ans+=1
            return max(root.val,left,right)
        dfs(root)
        return ans

        