# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        def dfs(node):
            nonlocal curr
            if node.left:
                left = dfs(node.left)
                if left is not None:
                    return left
            curr += 1
            if curr == k:
                return node.val

            if node.right:
                right = dfs(node.right)
                if right is not None:
                    return right
        
        return dfs(root)

            

