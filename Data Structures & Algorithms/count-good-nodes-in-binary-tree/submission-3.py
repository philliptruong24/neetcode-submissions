# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxsofar):
            nonlocal res
            if node.val >= maxsofar:
                res += 1
                maxsofar = node.val
            if node.left:
                dfs(node.left, maxsofar)
            if node.right:
                dfs(node.right, maxsofar)
        
        dfs(root, root.val)

        return res
        
            
