# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cnt = 0
        inDict = {}
        for i, value in enumerate(inorder):
            inDict[value] = i
        
        def build(left, right):
            if left > right:
                return None
            nonlocal cnt
            
            rootVal = preorder[cnt]
            cnt += 1

            root = TreeNode(rootVal)

            mid = inDict[rootVal]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
            
        
        return build(0, len(preorder) - 1)


