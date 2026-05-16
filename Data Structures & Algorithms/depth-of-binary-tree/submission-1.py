# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



        if not root:
            return 0

        res = 0
        stack = [(root, 1)]

        while stack:
            pair = stack.pop()
            res = max(res, pair[1])
            if pair[0].right:
                stack.append((pair[0].right, 1 + pair[1]))
            if pair[0].left:
                stack.append((pair[0].left, 1 + pair[1]))
        
        return res

