# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs, queue

        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            outer = 101

            for i in range(qLen):
                node = q.popleft()


                if node:
                    outer = node.val
                    q.append(node.left)
                    q.append(node.right)

            if outer != 101:
                res.append(outer)
                    
        return res
            