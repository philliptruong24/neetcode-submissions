# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        if root is None:
            return 0
        stack = [(root, root.val)]
        while stack:
            node, maxfar = stack.pop()
            if node.left:
                if node.left.val >= maxfar:
                    stack.append((node.left, node.left.val))
                    res += 1
                else:
                    stack.append((node.left, maxfar))
            if node.right:
                if node.right.val >= maxfar:
                    stack.append((node.right, node.right.val))
                    res += 1
                else:
                    stack.append((node.right, maxfar))
        
        return res
        
        
            
