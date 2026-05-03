# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int)
        def dfs(node, robbed_prev):
            if node == None:
                return 0

            if (node, robbed_prev) in dp:
                return dp[(node, robbed_prev)]
            
            res_skip = dfs(node.left, False) + dfs(node.right, False)

            if robbed_prev:
                result = res_skip
            else:
                result = dfs(node.left, True) + dfs(node.right, True) + node.val
                result = max(result, res_skip)
                

            
            dp[(node, robbed_prev)] = result
            return result

        return dfs(root, False)