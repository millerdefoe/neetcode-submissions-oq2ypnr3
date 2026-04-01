# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque()
        qQueue = deque()
        pQueue.append(p)
        qQueue.append(q)

        while pQueue and qQueue:
            pPop, qPop = pQueue.popleft(), qQueue.popleft()

            if pPop is None and qPop is None:
                continue

            if  pPop is None or qPop is None or (pPop.val != qPop.val):
                return False
            

            pQueue.append(pPop.left)

            pQueue.append(pPop.right)

            qQueue.append(qPop.left)

            qQueue.append(qPop.right)


        return True

