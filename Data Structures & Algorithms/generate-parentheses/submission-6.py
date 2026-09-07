class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, left, right):
            if left == n and right == n:
                res.append(curr)
                return

            if right != left:
                curr += ')'
                dfs(curr, left, right + 1)
                curr = curr[:-1]
                
            if left != n:
                curr += "("
                dfs(curr, left + 1, right)

        dfs("", 0, 0)
        return res