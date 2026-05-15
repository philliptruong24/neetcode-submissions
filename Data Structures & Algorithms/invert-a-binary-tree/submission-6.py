# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        # if root == None:
        #     return None

        # stack = [root]
        # while stack:
        #     temp = stack.pop()
        #     temp.left, temp.right = temp.right, temp.left

        #     if temp.right != None:
        #         stack.append(temp.right)
        #     if temp.left != None:
        #         stack.append(temp.left)
        
        # return root


        # BFS
        if root == None:
            return None
        queue = deque([root])
        while queue:
            temp = queue.popleft()
            temp.left, temp.right = temp.right, temp.left

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        
        return root

