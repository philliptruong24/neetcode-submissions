# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root == None:
                return True, 0
            
            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)
            if abs(leftHeight - rightHeight) > 1 or not leftBalanced or not rightBalanced:
                return False, 1 + max(leftHeight, rightHeight)
            else:
                return True, 1 + max(leftHeight, rightHeight)

    
        return dfs(root)[0]