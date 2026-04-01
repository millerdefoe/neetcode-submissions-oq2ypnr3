# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if q.val <= node.val <= p.val:
                return node

            if p.val <= node.val <= q.val:
                return node

            if node.val > p.val and node.val > q.val:
                queue.append(node.left)

            if node.val < p.val and node.val < q.val:
                queue.append(node.right)
            






