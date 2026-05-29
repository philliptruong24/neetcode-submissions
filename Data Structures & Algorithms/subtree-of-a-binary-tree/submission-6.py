# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        node = None
        while q:
            node = q.popleft()
            if node:
                if node.val == subRoot.val:
                    flag = True
                    stack = [(node, subRoot)]
                    while stack:
                        node1, node2 = stack.pop()
                        if not node1 and not node2:
                            continue
                        elif not node1 or not node2 or node1.val != node2.val:
                            flag = False
                            break

                        stack.append((node1.left, node2.left))
                        stack.append((node1.right, node2.right))
                    if flag:
                        return flag
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
        

            


