# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     Brute force
    #     if not root:
    #         return 0
        
    #     leftHeight = self.maxHeight(root.left)
    #     rightHeight = self.maxHeight(root.right)
    #     diameter = leftHeight + rightHeight
        
    #     sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    #     return max(sub, diameter)
        
    # def maxHeight(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))


        res = 0
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res





















