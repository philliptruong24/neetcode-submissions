# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cnt = 0
        indices = {val: idx for idx, val in enumerate(inorder)}
        def dfs(left, right):
            nonlocal cnt
            if left > right:
                return None
            

            rootVal = preorder[cnt]
            cnt += 1

            root = TreeNode(rootVal)
            mid = indices[rootVal]
            
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(preorder) - 1)


