# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return True, 0
            
            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)
            diff = abs(rightHeight - leftHeight)

            if rightBalanced and leftBalanced and diff <= 1:
                return True, 1 + max(rightHeight, leftHeight)
            
            else:
                return False, 1 + max(rightHeight, leftHeight)


        return dfs(root)[0]