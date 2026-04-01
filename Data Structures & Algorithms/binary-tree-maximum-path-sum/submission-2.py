# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #dfs recursive
        res = float("-inf")
        leftSum, rightSum = 0,0

        def dfs(node):
            if not node:
                return 0
            
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)

            newTotal = leftSum + rightSum + node.val

            nonlocal res 
            res = max(newTotal, res)

            return node.val + max(leftSum, rightSum)

        dfs(root)

        return res