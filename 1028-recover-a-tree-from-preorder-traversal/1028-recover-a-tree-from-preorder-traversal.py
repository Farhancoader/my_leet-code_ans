# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i =0
        n = len(traversal)
        root = None
        while i<n:
            dashes = 0
            while traversal[i]=="-":
                dashes+=1
                i+=1
            num = ""
            while i<n and traversal[i]!="-":
                num+=traversal[i]
                i+=1
            new = TreeNode(int(num))

            while len(stack)>dashes:
                stack.pop()
            if stack:
                top = stack[-1]
                if not top.left:
                    top.left = new
                else:
                    top.right = new
            else:
                root = new
            stack.append(new)
        return root
            

            