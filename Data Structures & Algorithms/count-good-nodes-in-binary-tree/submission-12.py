# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        res = 0
        while stack:
            node, maxfar = stack.pop()
            if node.val >= maxfar:
                res += 1
            newmax = max(node.val, maxfar)
            if node.left:
                stack.append((node.left, newmax))
            if node.right:
                stack.append((node.right, newmax))
        
        return res
