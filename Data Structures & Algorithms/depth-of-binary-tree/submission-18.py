# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            length = 0
            if node:
                length = 1 + max(dfs(node.left), dfs(node.right))
            
            res = max(length, res)
            return length
        
        dfs(root)

        return res

